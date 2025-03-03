import boto3
import csv
import logging

# Configuração de logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Inicializa clientes da AWS
session = boto3.Session(region_name='us-east-1')
s3_client = session.client('s3')
ses_client = session.client('ses')

def envio_email(event, context):
    try:
        # Obtém o nome do bucket e a chave do objeto do evento do S3
        bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
        object_key = event["Records"][0]["s3"]["object"]["key"]

        # Baixa o arquivo CSV do S3
        csv_file = s3_client.get_object(Bucket=bucket_name, Key=object_key)
        csv_content = csv_file['Body'].read().decode('utf-8').splitlines()

        # Processa o CSV
        users = csv.reader(csv_content)
        next(users)  # Pula o cabeçalho

        for user in users:
            if len(user) < 2:
                logger.warning(f"Linha inválida no CSV: {user}")
                continue

            user_name, email = user[0], user[1]
            send_email(user_name, email)

        return {"statusCode": 200, "body": "Emails enviados com sucesso!"}

    except Exception as e:
        logger.error(f"Erro ao processar o evento: {str(e)}")
        return {"statusCode": 500, "body": f"Erro interno: {str(e)}"}

def send_email(user_name, email):
    try:
        response = ses_client.send_email(
            Source="jogosdiarios.info@gmail.com",  # Email verificado no SES
            Destination={
                'ToAddresses': [email],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': 'UTF-8',
                        'Data': f"<html><head></head><body><h1>Olá, {user_name}!</h1><p>Seja bem-vindo!</p></body></html>"
                    },
                },
                'Subject': {
                    'Charset': 'UTF-8',
                    'Data': f'Hello, {user_name}!'
                },
            },
        )
        logger.info(f"Email enviado para {email}: MessageId={response['MessageId']}")
        return response['MessageId']
    except Exception as e:
        logger.error(f"Erro ao enviar email para {email}: {str(e)}")
