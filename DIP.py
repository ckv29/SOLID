from abc import ABC,abstractclassmethod

class Notifier(ABC):
    @abstractclassmethod
    def send(self,user,message):
        pass

class EmailSender(Notifier):
    def send(self, user, message):
        print(f"Отправка email для {user.email}: {message}")


class SMSSender(Notifier):
    def send(self, user, message):
        print(f"Отправка SMS на номер {user.phone}: {message}")



class NotificationService:
    def __init__(self, notifiers : Notifier):
        self.notifiers = notifiers
    
    def notify_user(self, user, message):
        contact_type = user.contact_preference
        self.notifiers[contact_type].send(user,message)


class User:
    def __init__(self, name, email=None,phone=None, contact_preference = "email"):
        self.name = name
        self.email = email
        self.phone = phone
        self.contact_preference = contact_preference


es = EmailSender()
ss = SMSSender()

notifiers = {
    "email" : es,
    "sms" : ss
}

user1 = User("John","john@mail.ru",contact_preference="email")
ns1 = NotificationService(notifiers)
ns1.notify_user(user1,"Привет!")

user2 = User("BibaBoba","bb@mail.ru","+780006545",contact_preference="sms")
ns2 = NotificationService(notifiers)
ns2.notify_user(user2,"Привет!")
