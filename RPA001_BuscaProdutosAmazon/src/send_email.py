import smtplib
import csv
import logging
from email.message import EmailMessage
from src.config import EMAIL_FROM, EMAIL_PASSWORD, EMAIL_TO, SMTP_SSL, SMTP_PORT
logger = logging.getLogger(__name__)

def salvar_e_enviar(dados, termo_busca):
    arquivo = f".\\output\\relatorio_produto_{termo_busca}.csv"
    
    # Salvar CSV (UTF-16 + Delimitador ';' para Excel Brasil)
    with open(arquivo, "w", newline="", encoding="utf-16") as f:
        writer = csv.DictWriter(f, fieldnames=["titulo", "preco"], delimiter=';')
        writer.writeheader()
        writer.writerows(dados)

    # Configurar E-mail
    msg = EmailMessage()
    msg["Subject"] = f"Relatório RPA Amazon: {termo_busca}"
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg.set_content(f"Segue anexo o relatório para a busca: {termo_busca}.\nTotal de itens: {len(dados)}")

    with open(arquivo, "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=arquivo)

    # Envio via SMTP_SSL (Porta 465)
    try:
        with smtplib.SMTP_SSL(SMTP_SSL, SMTP_PORT) as smtp:
            smtp.login(EMAIL_FROM, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("Processo finalizado e e-mail enviado!")
        logger.info(f"Processo finalizado e e-mail enviado!")
    except Exception as e:
        print(f"Erro no envio do e-mail: {e}")
        logger.info(f"Erro no envio do e-mail: {e}")