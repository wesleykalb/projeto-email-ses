# Projeto Serverless: Envio de Emails via CSV

Este projeto é uma aplicação serverless que envia emails para uma lista de usuários a partir de um arquivo CSV.

## Como Funciona

1. Faça upload de um arquivo CSV para o bucket S3 configurado.
2. A função Lambda é acionada e processa o CSV.
3. Os emails são enviados para os endereços contidos no CSV.

## Tecnologias

- AWS Lambda
- Amazon S3
- Amazon SES
- Python 3.8
- Serverless Framework

## Como Executar

### Pré-requisitos

- Node.js e Serverless Framework instalados.
- Conta AWS com permissões para S3, Lambda e SES.

### Deploy

```bash
serverless deploy