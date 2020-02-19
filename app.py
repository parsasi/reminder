import ReminderClass
import NotepadClass
import Helpers
Notepad = NotepadClass.Notepad
Reminder = ReminderClass.Reminder
Helpers = Helpers.Helper

q = False
Helper = Helpers() 
while(q == False):
    command = Helper.printMenu()
    q = (command == "7")  
    if(q):break
    if(command == "1"):
        Helper.getAllNotes()
    elif(command == "2"):
        Helper.searchAllReminders()
    elif(command == "3"):
        Helper.addNewNote()
    elif(command == "4"):
        Helper.modifyANote()
    elif(command == "5"):
        print(command)
    elif(command == "6"):
        print(command)
    else:
        continue
