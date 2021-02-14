zoomAddress= "C:\\Users\\Yogesh\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
sleepTimeAppStart = 5
sleepTimeClick = 5
sleepTimeJoin = 30

keyboardDelay = 0.2

appMode = "Light"

userDisplayNameEnable = False
userDisplayName = "Akshat Tilak"

connectAudioEnable = True
connectVideoEnable = True

chatsRefreshRate = 1000
chatsLinksSaveEnable = True
chatsAllSaveEnable = True
chatsLinkNotification = True
chatsLinkNotificationFrequency = 500
chatsLinkNotificationDuration = 1000
chatOutputDirectory = "chats/"

settingAttributesName =["Zoom Address", "Zoom Mode", "Delay for Zoom to open","Delay for Zoom to connect",
"Delay after mouse click", "Delay between Key press", "Change user display name enabled", "User display name",
"Connect to audio in meeting", "Connect to video in meeting", "Chats refresh rate","Chats output directory path",
"Save all chats", "Save links from chats", "Links notification enabled", "Links notification beep frequency", 
"Link notification beep duration"]

settingAttributesValues =[zoomAddress, appMode, sleepTimeAppStart, sleepTimeJoin, sleepTimeClick, keyboardDelay,
userDisplayNameEnable, userDisplayName, connectAudioEnable, connectVideoEnable, chatsRefreshRate, chatOutputDirectory,
chatsAllSaveEnable, chatsLinksSaveEnable, chatsLinkNotification, chatsLinkNotificationFrequency, chatsLinkNotificationDuration]

def update():
    global settingAttributesValues 
    settingAttributesValues = [zoomAddress, appMode, sleepTimeAppStart, sleepTimeJoin, sleepTimeClick, keyboardDelay,
    userDisplayNameEnable, userDisplayName, connectAudioEnable, connectVideoEnable, chatsRefreshRate, chatOutputDirectory,
    chatsAllSaveEnable, chatsLinksSaveEnable, chatsLinkNotification, chatsLinkNotificationFrequency, chatsLinkNotificationDuration]


def changeSettings():
    update()
    saveFile()
    for i in range(len(settingAttributesName)):
        print("{}-> {} : {}".format(i+1, settingAttributesName[i], settingAttributesValues[i]))
    print("18-> RETURN BACK")
    print("SYS>> Select an attribute to change")
    cmd = input("USER>> ").replace(" ","")
    if cmd =="1":
        global zoomAddress
        print("SYS>> Please provide path for zoom executable file.")
        zoomAddress = input("USER>>")
        print(zoomAddress)
    elif cmd=="2":
        global appMode
        print("SYS>> Please provide app mode (Either Light or Dark)")
        print("SYS>> Currently Dark mode is not supported, you will have to add images for dark mode")
        while True:
            inp = input("USER>> ").lower()
            if inp == "light":
                appMode = "Light"
                break
            elif inp == "dark":
                appMode == "Dark"
                break
            else:
                print("SYS>> Please provide valid input")
    elif cmd=="3":
        global sleepTimeAppStart
        print("SYS>> Please provide delay for zoom to open (in milliseconds)")
        while True:
            inp = input("USER>> ")
            if inp.isnumeric():
                sleepTimeAppStart = int(inp)
                break
            else:
                print("SYS>> Please provide valid input")
    elif cmd=="4":
        global sleepTimeJoin
        print("SYS>> Please provide delay to join zoom meeting (in milliseconds)")
        while True:
            inp = input("USER>> ")
            if inp.isnumeric():
                sleepTimeJoin = int(inp)
                break
            else:
                print("SYS>> Please provide valid input")
    elif cmd=="5":
        global sleepTimeClick
        print("SYS>> Please provide delay after every mouse click (in milliseconds)")
        while True:
            inp = input("USER>> ")
            if inp.isnumeric():
                sleepTimeClick = int(inp)
                break
            else:
                print("SYS>> Please provide valid input")
    elif cmd=="6":
        global keyboardDelay
        print("SYS>> Please provide delay between each keyboard click (in sseconds)")
        while True:
            inp = input("USER>> ")
            if inp.isnumeric():
                keyboardDelay = int(inp)
                break
            else:
                print("SYS>> Please provide valid input")
    elif cmd=="7":
        global userDisplayNameEnable
        print("SYS>> Please provide if the  username name is to be changed before joining meeting")
        while True:
            inp = input("USER>> ").lower()
            if inp == "true":
                userDisplayNameEnable = True
                break
            elif inp == "false":
                userDisplayNameEnable = False
                break
            else:
                print("SYS>> Please provide valid input")
    elif cmd=="8":
        global userDisplayName
        print("SYS>> Please provide user name to display in meeting")
        userDisplayName = input("USER>> ")
    elif cmd=="9":
        global connectAudioEnable
        print("SYS>> Please provide if the audio is to be connected.")
        while True:
            inp = input("USER>> ").lower()
            if inp == "true":
                connectAudioEnable = True
                break
            elif inp == "false":
                connectAudioEnable = False
                break
            else:
                print("SYS>> Please provide valid input")
    elif cmd=="10":
        global connectVideoEnable
        print("SYS>> Please provide if the audio is to be connected.")
        while True:
            inp = input("USER>> ").lower()
            if inp == "true":
                connectVideoEnable = True
                break
            elif inp == "false":
                connectVideoEnables = False
                break
            else:
                print("SYS>> Please provide valid input")
    elif cmd=="11":
        global chatsRefreshRate
        print("SYS>> Please provide chat refresh rate (in milliseconds)")
        while True:
            inp = input("USER>> ")
            if inp.isnumeric():
                chatsRefreshRate = int(inp)
                break
            else:
                print("SYS>> Please provide valid input")
    elif cmd=="12":
        global chatOutputDirectory
        print("SYS>> Please provide output directory to store chats")
        chatOutputDirectory = input("USER>> ")
    elif cmd=="13":
        global chatsAllSaveEnable
        print("SYS>> Please provide if all chats are to be stored.")
        while True:
            inp = input("USER>> ").lower()
            if inp == "true":
                chatsAllSaveEnable = True
                break
            elif inp == "false":
                chatsAllSaveEnable = False
                break
            else:
                print("SYS>> Please provide valid input")
    elif cmd=="14":
        global chatsLinksSaveEnable
        print("SYS>> Please provide if all links in the chats are to be stored.")
        while True:
            inp = input("USER>> ").lower()
            if inp == "true":
                chatsAllSaveEnable = True
                break
            elif inp == "false":
                chatsAllSaveEnable = False
                break
            else:
                print("SYS>> Please provide valid input")
    elif cmd=="15":
        global chatsLinkNotification
        print("SYS>> Please provide if notifications are to be given for new links in the chat")
        while True:
            inp = input("USER>> ").lower()
            if inp == "true":
                chatsLinkNotification = True
                break
            elif inp == "false":
                chatsLinkNotification = False
                break
            else:
                print("SYS>> Please provide valid input")
    elif cmd=="16":
        global chatsLinkNotificationFrequency
        print("SYS>> Please provide frequency of beep for notification (in hz between 37 to 32767)")
        while True:
            inp = input("USER>> ")
            if inp.isnumeric() and 37<int(inp)<32767:
                chatsRefreshRate = int(inp)
                break
            else:
                print("SYS>> Please provide valid input")
    elif cmd=="17":
        global chatsLinkNotificationDuration
        print("SYS>> Please provide duration of beep for notification (in milliseconds)")
        while True:
            inp = input("USER>> ")
            if inp.isnumeric():
                chatsLinkNotificationDuration = int(inp)
                break
            else:
                print("SYS>> Please provide valid input")
    elif cmd=="18":
        return(-1)
    else:
        print("SYS>> Please provide valid input")


def saveFile():
    global settingAttributesValues
    with open("settings.txt","w") as f:
        f.write(",".join(list(str(i) for i in settingAttributesValues)))

def loadFile():
    global zoomAddress
    global appMode
    global sleepTimeAppStart
    global sleepTimeJoin
    global sleepTimeClick
    global keyboardDelay
    global userDisplayNameEnable
    global userDisplayName
    global connectAudioEnable
    global connectVideoEnable
    global chatsRefreshRate
    global chatOutputDirectory
    global chatsAllSaveEnable
    global chatsLinksSaveEnable
    global chatsLinkNotification
    global chatsLinkNotificationFrequency
    global chatsLinkNotificationDuration
    with open("settings.txt","r") as f:
        temp = f.read().split(",")
    zoomAddress= temp[0]
    appMode= temp[1]
    sleepTimeAppStart= int(temp[2])
    sleepTimeJoin= int(temp[3])
    sleepTimeClick= int(temp[4])
    keyboardDelay= float(temp[5])
    userDisplayNameEnable = bool(temp[6])
    userDisplayName= temp[7]
    connectAudioEnable= bool(temp[8])
    connectVideoEnable= bool(temp[9])
    chatsRefreshRate= int(temp[10])
    chatOutputDirectory= temp[11]
    chatsAllSaveEnable= bool(temp[12])
    chatsLinksSaveEnable= bool(temp[13])
    chatsLinkNotification= bool(temp[14])
    chatsLinkNotificationFrequency= int(temp[15])
    chatsLinkNotificationDuration= int(temp[16])
    update()

try:
    with open("settings.txt","r") as f:
        pass
except:
    saveFile()
loadFile()
print(sleepTimeAppStart)
