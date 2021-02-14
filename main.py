import zoomFunctions
import settings
import winsound
import time
from datetime import datetime
import calendar

def mainProgram():
    f = open("meet.txt", "r")
    lst = f.readlines()
    while True:
        now = datetime.now().strftime("%H:%M")
        my_date = datetime.today()
        day_now = calendar.day_name[my_date.weekday()]
        for x in lst:
            x = list(map(str, x.split(',')))
            if x[0] == day_now and x[1] == now:
                m_id = x[3]
                if "\n" in x[4]:
                    m_pswd = x[4][:len(x[4])-1]
                else:
                    m_pswd = x[4]
                print(meetingSession(m_id, m_pswd,x[2]))
                time.sleep(60)

            if x[2]== now:
                zoomFunctions.endmeet()
                time.sleep(60)
            time.sleep(60)
            print(zoomFunctions.chats())


def mainMenu():
    print("+------------------------------------------------+")
    print("+------------------------------------------------+")
    print("|                    ZOOM BOT                    |")
    print("+------------------------------------------------+")
    print("+---+--------------------------------------------+")
    print("| 1 | Start program                              |")
    print("+---+--------------------------------------------+")
    print("| 2 | Change Settings                            |")
    print("+---+--------------------------------------------+")
    print("| 3 | Troubleshooting                            |")
    print("+---+--------------------------------------------+")
    print("| 4 | Exit                                       |")
    print("+---+--------------------------------------------+")
    print("| Select an option                               |")
    print("+---+--------------------------------------------+")
    cmd = input("USER>> ").replace(" ","")
    if cmd =="1":
        mainProgram()
    elif cmd == "2":
        while True:
            res = settings.changeSettings()
            if res==-1:
                break
    elif cmd=="3":
        print("+------------------------------------------------+")
        print("| 1-> If at any point the app is not functioning |")
        print("| properly, then try changing the pictures in    |")
        print("| the resources folder.                          |")
        print("+------------------------------------------------+")
        print("| Hopefully the troubleshooting is helful        |")
        print("+------------------------------------------------+")
        return
    elif cmd=="4":
        exit
    else:
        print("SYS>> Please provide a valid input")
        return




def meetingSession(meetingID, meetingPassword, endTime):
    joinCode = zoomFunctions.joinMeeting(meetingID, meetingPassword)
    if joinCode==1:
        print("Meeting joined sucessfully")
    else:
        print("Meeting join failed\nError:",joinCode)
        return()
    Links = []
    while datetime.now().strftime("%H:%M")!=endTime:
        #chats = zoomFunctions.chats()
        #Links = chats[1]
        #if settings.chatsLinkNotification:
        #    if Links!= chats[1]:
        #        winsound.Beep(settings.chatsLinkNotificationFrequency, settings.chatsLinkNotificationDuration)
        #if settings.chatsAllSaveEnable:
        #    with open("{}AllChats{}.txt".format(settings.chatOutputDirectory, str(endTime).replace(":",""), "w")) as f:
        #        for i in chats[0]:
        #            f.write(i)
        #if settings.chatsLinksSaveEnable:
        #    with open("{}Links{}.txt".format(settings.chatOutputDirectory, str(endTime).replace(":",""), "w")) as f:
        #        for i in chats[1]:
        #            f.write(i)
        time.sleep(settings.chatsRefreshRate)
    zoomFunctions.endmeet()


while True:
    mainMenu()

