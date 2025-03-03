from src.handler import send_email

def test_send_email():
    # Chama a função send_email com um email verificado no SES
    message_id = send_email("Teste", "teste@dominio.com")  # Substitua por um email verificado no SES

    # Verifica se o MessageId foi retornado
    assert isinstance(message_id, str)
