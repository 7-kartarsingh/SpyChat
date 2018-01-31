class Spy:

  def __init__(self, name, salutation, age, rating):
    self.name = name
    self.salutation = salutation
    self.age = age
    self.rating = rating
    self.is_online = True
    self.chats = []
    self.current_status_message = None

spy = Spy("BOND","Mr.",29,4.6)

friend_one = Spy("Bob","Mr.", 23, 4.7)
friend_two = Spy("Peter","Mr.", 25, 4.5)
friend_three = Spy("Suzi","Mrs.", 24, 4.8)

Friends = [friend_one,friend_two,friend_three]


class ChatMessage:

    def __init__(self, message,datetime, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me
