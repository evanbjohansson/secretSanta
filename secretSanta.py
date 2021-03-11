import random 
import os
from twilio.rest import Client

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

class Person:
    def __init__(self,name,phone,partner=None):
        self.name=name
        self.phone=phone
        self.partner=partner
        self.recipient=None
    def addRecipient(self,recipient):
        self.recipient=recipient
    def sendText(self):
        message = client.messages \
                .create(
                     body="Ho Ho Ho, I hope your tree is lit and bells are jingled because for this year’s secret santa you’ll be getting a gift for ***" + self.recipient + "***! It's Jaime the elf here, reminding you not to share your results or you’ll be put on my naughty list ;) merry xxxmas and happy shopping!",
                     from_='+15555555555',  #insert twilio given number here
                     to=self.phone
                 )

gifters = [
    Person("Ethan","+15555555555","Kimi"),  #redacted personal info
    Person("Kimi","+15555555555","Ethan"),
    Person("Kevin","+15555555555","Haylee"),
    Person("Haylee","+15555555555","Kevin"),
    Person("Jake","+15555555555","Betty"),
    Person("Betty","+15555555555","Jake"),
    Person("Edward","+15555555555","Amy"),
    Person("Amy","+15555555555","Edward"),
    Person("Ester","+15555555555"),
    Person("Josue","+15555555555"),
    Person("Jefferson","+15555555555")
]

recipients = set()   #set of names
for gifter in gifters:
    recipients.add(gifter.name)    #add each name from gifters list

for x in range(len(gifters)):
    choices = recipients.difference({gifters[x].name,gifters[x].partner})    #choices set excludes own name and partner's name 
    if x == len(gifters)-2 and gifters[x+1].name in choices:    #if last person in gifters list hasnt been chosen, 2nd to last must chose them
        recipient = gifters[x+1].name
    else:
        recipient = random.sample(choices,1)[0]      #take only element in the random sample list
    recipients.remove(recipient)
    gifters[x].addRecipient(recipient)
    gifters[x].sendText()