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
        #Listing notes
        Helper.getAllNotes()
    elif(command == "2"):
        #Search in notes
        Helper.searchAllReminders()
    elif(command == "3"):
        #Add to notes
        Helper.addNewNote()
    elif(command == "4"):
        #Editing notes
        Helper.modifyANote()
    elif(command == "5"):
        Helper.saveNote()
    elif(command == "6"):
        Helper.openNote()
    else:
        continue
