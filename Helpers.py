import NotepadClass
import ReminderClass
import re
Reminder = ReminderClass.Reminder
class Helper:
    def __init__(self):
        #Gives access to all Notepad functionalities
        self.notepad =  NotepadClass.Notepad
    def printMenu(self):
        print("""Menu:\n\t1. Show all reminders\n\t2. Search all reminders\n\t3. Add reminders\n\t4. Modify reminders\n\t5. Export reminders\n\t6. Import reminders\n\t7. Exit\nYour Choice:\t""")
        return input()
    def getAllNotes(self):
        allNotes = self.notepad.showNotes()
        self.output(allNotes)
    def addNewNote(self):
        print("""Enter a reminder:""")
        newReminderText = input()
        if(not newReminderText):
            return
        print("""Enter tags, comma seperated if multiple:""")
        newReminderTagsText = input()
        try:
            newReminderTags  = newReminderTagsText.replace(',',' ').split()
        except:
            return
        newReminder = Reminder(newReminderText , newReminderTags)
        self.notepad.addNote(newReminder)
    def searchAllReminders(self):
        print("""Search: """)
        searchTerm = input()
        return self.output(self.notepad.searchNote(searchTerm))
    def modifyANote(self):
        print("""Enter the note id:""")
        newReminderId = input()
        print("""Enter the new text:""")
        newReminderText = input()
        print("""Enter new tags:""")
        newReminderTagsText = input()
        newReminderTags  = newReminderTagsText.replace(',',' ').split()
        newReminderTags  = newReminderTagsText.replace(',',' ').split()
        newReminder = Reminder(newReminderText , newReminderTags)
        newReminder.id = newReminderId
        self.notepad.modifyNote(newReminder)
    def saveNote(self):
        print("""Please enter a name for your file:""")
        name = input()
        self.notepad.exportNote(name)
    def openNote(self):
        print("""Please enter the file name you wish to open""")
        name = input()
        self.notepad.importName(name)
    def output(self,listOfItems):
        for item in listOfItems:
            tags = ""
            for itemTag in item.tags:
                tags = tags + F" {itemTag} "
            print(F"ID:{item.id}\n{item.text}\nTags:{tags}\n______________________\n")