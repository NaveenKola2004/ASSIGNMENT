#1. Smart Home Mode Selection
#2. Virtual Assistant Response
message=input("Enter the message : ")

if(message.startswith('Hey')):
    print("How can i help  you?")
elif('weather' in message):
    print("Fetching weather details...")
elif(message.endswith('?')):
    print("set me find that for you.")
else:
    print("I'm here if you need anything.")

#3. Smart Notification Filter

sender=input("Enter the message : ")

if sender in ["Bank",'Emergency Services','Government']:
    print("important")
elif sender in ["Facebook", "Instagram","Twitter"]:
    print("Social")
elif sender in ["Boss","HR","Team"]:
    print("Work")
else:
    print("Other")

#4. Digital Lock Access

password=input("Enter the password : ")

if (password.startswith('9')):
    print("Admin Access Granted")
elif(password.startswith('1') or password.startswith('2')):
    print("User Access Granted")
elif(password.endswith('0')):
    print("Guest Access Granted")
else:
    print("Access Denied")

#5. Smart Music Player Mode

song=input("Enter the song name : ")

if (song in ["Pop", "EDM","Dance"]):
    print("Party Mode")
elif(song in ["Classical", "Jazz","Acoustic"]):
    print("Relax Mode")
elif(song in ["Rock","Hip-Hop","Metal"]):
    print("Workout Mode")
else:
    print("Default Mode")

#6. Automated Email Response

subject=input("Enter the subject : ")
if (subject in["leave", "vacation", "holiday"]):
    print("Out of office")
elif(subject in ["urgent","ASAP"]):
    print("Urgent Response Required")
elif(subject in [ "help", "question","support"]):
    print("General Inquiry")
else:
    print("No Action Needed")

#7. Smart Car Mode Selection

fuel=int(input("Enter the fuel percentage : "))
speed=int(input("Enter the speed : "))
air=input("air conditioning ON/OFF : ")
if(fuel <20 and speed < 60 ):
    print("Eco Mode")
elif(speed>100):
    print("sport Mode")
elif(air == "on" and [speed >=60 and speed <=100]):
    print("Comfort Mode")
else:
    print("Normal Mode")

#8. Smart Security Camera Detection

object=input("Enter the Object : ")
time=int(input("Entr the time : "))
if (object in ["person"]):
    print("Alert: Intruder Detected")
elif(object in ["Dog", "Cat","Bird"]):
    print("Animal Detected")
elif(object in ["Car","Bike"]):
    print("Vehicle Detected")
else:
    print("No Threat Detected")
