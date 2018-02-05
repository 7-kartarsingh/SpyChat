from datetime import datetime
import time

class Spy:
    def __init__(self,name,salutation,age,rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

class ChatMessage:
    def __init__(self,message,sent_by_me):
        self.message=message
        t = datetime.now()
        t = time.mktime(t.timetuple())
        self.time=time.strftime("%I:%M %p",time.localtime(t))
        self.sent_by_me=sent_by_me

spy= Spy('Ghoul','Mr',26, 4.3)
friend_one = Spy("Agent99","Mr.",27, 4.7)
friend_two = Spy("Agent Jane","Ms.", 23, 4.6)
friend_three = Spy("Agent Kay","Mr.", 24, 4.8)

friends = [friend_one, friend_two, friend_three]
chat= ChatMessage("hi",True)
chats=[]