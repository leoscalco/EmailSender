#!/usr/bin/python
# -*- coding: UTF-8 -*-
from EmailSender import *

emailsender = EmailSender('smtp.gmail.com', 587)

try:
    emailsender.login("fromaddr", "password")
    emailsender.send_with_attachment("toaddr", "subject", "body", "file_path")
    emailsender.quit()
except Exception, e:
    print "Error!"
    print str(e)
