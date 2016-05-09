# EmailSender
A python application to send emails

Code based on this: http://naelshiab.com/tutorial-send-email-python/

<b>Remember to allow "less secure apps" on Gmail</b>

###### Simple mail

```python
from EmailSender import *

emailsender = EmailSender('smtp.gmail.com', 587) # mail server, port 
emailsender.login("fromaddr@email.com", "password") # login with from, password
emailsender.send("toaddr@email.com", "body")  # to address, message
emailsender.quit() # logout
```

###### Sending attachments

```python
from EmailSender import *

emailsender = EmailSender('smtp.gmail.com', 587) # mail server, port 
emailsender.login("fromaddr@email.com", "password") # login with from, password
emailsender.send_with_attachment("toaddr@email.com", "subject", "body", "file_path") # to, subject, body, path_file
emailsender.quit() # logout
```
