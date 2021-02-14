THIS PROJECT WAS SUBMITTED TO WIT+BYLD HACKATHON 2021

ZOOM_BOT
With online classes going on one of the things that has been irritating for all of us is looking around for zoom links every week for the same classes.
Well with zoom_bot you can join zoom meetings automatically by specifying which meets to join and when.

Team Members:
Yogesh Kaushik
Akshat Tilak
Utkarsh Arora

First off :
1. open the meet text file.
2. Add comma seperated values in the following order:
	Day,Meeting start time(24hr format),Meeting End Time(24hr format), meetingid, meeting password
3. for multiple meets just keep switching lines after meeting password for all entries
	eg.
		Sunday,15:30,15:40,1234904810,BUSJW
		Sunday,15:41,16:30,1234904810,BUSJW 
4. Start the main.py file.
5. Firstly navigate to settings and change the file path to your own zoom file.
+------------------------------------------------+
+------------------------------------------------+
|                    ZOOM BOT                    |
+------------------------------------------------+
+---+--------------------------------------------+
| 1 | Start program                              |
+---+--------------------------------------------+
| 2 | Change Settings                            |
+---+--------------------------------------------+
| 3 | Troubleshooting                            |
+---+--------------------------------------------+
| 4 | Exit                                       |
+---+--------------------------------------------+
| Select an option                               |
+---+--------------------------------------------+


6. Then change any settings the way you want.
1-> Zoom Address : C:\\Users\\Akshat Tilak\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe
2-> Zoom Mode : Light
3-> Delay for Zoom to open : 5
4-> Delay for Zoom to connect : 30
5-> Delay after mouse click : 5
6-> Delay between Key press : 0.2
7-> Change user display name enabled : True
8-> User display name : Akshat Tilak
9-> Connect to audio in meeting : True
10-> Connect to video in meeting : True
11-> Chats refresh rate : 1000
12-> Chats output directory path : chats/
13-> Save all chats : True
14-> Save links from chats : True
15-> Links notification enabled : True
16-> Links notification beep frequency : 500
17-> Link notification beep duration : 1000
18-> RETURN BACK
SYS>> Select an attribute to change


7. Now start.
8. Do not close the program and if the details given are valid for the zoom meetings then you will automatically join and exit.  
9. The program can filter and notify you if there are any links that have been posted on the chat box.
10. User can also save these. 
