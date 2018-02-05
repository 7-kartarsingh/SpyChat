from spy_details import spy,friends,Spy,ChatMessage,chats
from steganography.steganography import Steganography
from datetime import datetime
import csv

print "Ready for the Thrilling Experience, Lets get into it ! "

STATUS_MESSAGES=["Never give up without a fight','In a world full of Fish, Be Shark','YOUR MIND IS A WEAPON, ALWAYS KEEP IT LOADE"]

response= raw_input("Do you  want to continue as "+spy.salutation+" "+spy.name+ " (Y/N)?")

#Loading friends
def load_friends():
    with open('friends.csv', 'rU') as friends_data:
        reader = csv.reader(friends_data,delimiter=',', quotechar='"')

        for row in reader:
            spy = Spy(row[0],row[1],row[2],row[3])
            friends.append(spy)

# Loading chats
def load_chats():
    with open('chats.csv', 'rU') as chats_data:
        reader = csv.reader(chats_data,delimiter=',', quotechar='"')

        for row in reader:
            chat = ChatMessage(row[0], row[1])
            chats.append(spy)

#Chat messenger starts
def start_chat(spy):
    load_friends()
    load_chats()
    show_menu=True
    current_status_message = None
    while show_menu==True:
        # menu options
        menu_choices= "What do you want to do ? \n 1. Add a status update\n 2. Add a friend\n 3. Select a friend\n 4. Send a message\n 5. Read a message\n6. Closing Application"
        menu_choice= int(raw_input(menu_choices))
        if menu_choice==1:
           current_status_message= add_status(current_status_message)
        elif menu_choice==2:
            number_of_friends=add_friend()
            print "You have %d friends" %(number_of_friends)
        elif menu_choice==3:
            select_friend()
        elif menu_choice==4:
            send_message()
        elif menu_choice==5:
            read_message()
        else:
            show_menu=False
    print "Bye! Hope to see you back Soon"

# Function to  add status
def add_status(current_status_message):
    if current_status_message != None:
        print "Your Current status message is " + current_status_message + "\n"
    else:
        print "You  don't have any current status message"
    default= raw_input("Do you want to select from older status?(y/n)")
    if default.upper()== "N":
        new_status_message= raw_input("What status message you want to set?")
        if len(new_status_message)>0:
            updated_status_message=new_status_message
            STATUS_MESSAGES.append(updated_status_message)
    elif default.upper()== "Y":
        item_position=1
        for message in STATUS_MESSAGES:
            print str(item_position)+" "+message
            item_position=item_position+1
        message_selection= int(raw_input("\nChoose from the above staus messages"))
        if len(STATUS_MESSAGES)>= message_selection:
            updated_status_message=STATUS_MESSAGES[message_selection-1]
    return updated_status_message

# Function to add friend
def add_friend():

    Spy.name = raw_input("Please add your friend's name: ")
    Spy.salutation = raw_input("Are they Mr. or Ms.?: ")

    Spy.name = Spy.salutation + " " + Spy.name

    Spy.age = int(raw_input("Age?"))

    Spy.rating = float(raw_input("Spy rating?"))
    if len(Spy.name) > 0 and Spy.age > 12 and Spy.rating >= spy.rating:
        friends.append(Spy)
        print 'Friend Added!'
        # saving friends to friends.csv file
        with open('friends.csv', 'ab') as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([Spy.name,Spy.salutation,Spy.age,Spy.rating])

    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends)

# Function to  choose friend
def select_friend():
  item_number = 0

  for friend in friends:
    print '%d %s' % ((item_number + 1), friend.name)

    item_number = item_number + 1

  friend_choice = input("Choose from your friends")
  friend_choice_position=friend_choice-1
  f = friends[friend_choice_position]
  return  f


# Function to send message
def send_message():
    friend_choice= select_friend()
    original_image = raw_input("Image should be of .JPEG, .PNG, .JPG format .What is the name of the image?")
    if original_image.upper().endswith(".JPEG") or original_image.upper().endswith(".PNG") or original_image.upper().endswith(".JPG"):
     output_path = 'output.jpg'
    text = raw_input("What do you want to say?")
    #encode the message in image form
    Steganography.encode(original_image, output_path, text)
    ch=ChatMessage(text,True)
    (friend_choice.chats).append(ch)
    if "Save me" in text.capitalize() or "SOS" in text.upper() or "Help" in text.capitalize():
        print "Things are not working out here. Need someone here ASAP."
    print "Your secret message is ready"
    # save the chats to chats.csv file
    with open('chats.csv', 'ab') as chats_data:
        writer = csv.writer(chats_data)
        writer.writerow([ch.message,ch.time])

# function to read message
def read_message():
    sender = select_friend()
    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)     # decode the encoded message
    # check for special message
    if "Save me" in secret_text.capitalize() or "SOS" in secret_text.upper() or "Help" in secret_text.capitalize():
        print "Things are not going in right Direction."
    c= ChatMessage(secret_text,False)
    (sender.chats).append(c)
    print "Your secret message has been saved"


if response.upper()=="Y":
    print "App has started"
    start_chat(spy)
else:

    # Add a new spy with all details
    Spy.name = raw_input("Welcome to spy chat, What's your name Agent?  ")
    if len(Spy.name) > 0:
        print 'Welcome ' + Spy.name + '. Glad to have you back with us.'
        Spy.salutation = raw_input("Should I call you Mr or Ms ? ")
        Spy.name = Spy.salutation + " " + Spy.name
        print "Ok then ! " + Spy.name + ". Please tell more about Yourself"
    else :
        print "Invalid name. Please Try again."

    Spy.age= (int)(raw_input(" What is your age? "))

    if Spy.age>12 and Spy.age<50:
        Spy.rating= (float)(raw_input(" what is your spy rating "))
        if Spy.rating > 4.5:
            print 'Woah Virtuoso!'
        elif Spy.rating > 3.5 and Spy.rating <= 4.5:
            print 'Decent...'
        elif Spy.rating >= 2.5 and Spy.rating <= 3.5:
            print 'Their is always the scope of improvement'
        else:
            print 'Oopsi. Try hard and come back with a BANG'

        print "Authentication complete. Welcome " + Spy.name + " age: " + (str)(Spy.age) + " and rating of: " + (str)(
            Spy.rating) + "  Hope you will have an amazing journey"

    else:
        print "Sorry invalid age"
    start_chat(Spy)
