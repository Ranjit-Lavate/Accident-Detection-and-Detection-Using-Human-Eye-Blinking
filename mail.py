import smtplib
from email.message import EmailMessage
import imghdr

Sender_Email = "ranjitlavate1801@gmail.cpm"
Reciever_Email = "ranjitlavate0118@gmail.com"
Password ='iall fqye demt vimm'
newMessage = EmailMessage("Euu Project is Done")    #creating an object of EmailMessage class
newMessage['Subject'] = "Test Email from Accident Detection" #Defining email subject
newMessage['From'] = Sender_Email  #Defining sender email
newMessage['To'] = Reciever_Email  #Defining reciever email


#import requests 
#api_address = "http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
        
#import json
#location_req_url='http://api.ipstack.com/103.51.95.183?access_key=a7003977af457525708100fca423928d'
#r = requests.get(location_req_url)
#location_obj = json.loads(r.text)
        
#lat = location_obj['latitude']
#lon = location_obj['longitude']
#latitude = lat
#longitude = lon
#print(str(latitude))
#print(str(longitude))


newMessage.set_content('Hi,Accident detected.Please help me urgently...') #Defining email body

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login(Sender_Email, Password)              
    smtp.send_message(newMessage)












# # -*- coding: utf-8 -*-
# """
# Created on Thu Apr  4 15:09:56 2024

# @author: ABHIJIT
# """

# import smtplib
# from email.message import EmailMessage

# import smtplib
# from email.message import EmailMessage

# SENDER_EMAIL = "ranjitlavate0118@gmail.com"
# APP_PASSWORD = "uoyi qdud dcng eqqb"


# print("Mail Start")
# msg = EmailMessage()
# msg['Subject'] = "accident detected"
# msg['From'] = SENDER_EMAIL
# msg['To'] = "ganeshwalunjkar031@gmail.com"
# msg.set_content('accident detected')

# # with open('/home/pi/Face_Attendance_with_Excel_Sheet/Student_to_excel.xls', 'rb') as f:
# #         file_data = f.read()
# # msg.add_attachment(file_data, maintype="application", subtype="vnd.ms-excel", filename='/home/pi/Face_Attendance_with_Excel_Sheet/Student_to_excel.xls')

# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#         smtp.login(SENDER_EMAIL, APP_PASSWORD)
#         smtp.send_message(msg)
#         print("Mail send successfully")

