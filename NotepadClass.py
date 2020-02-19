class Notepad:
    allReminders = []
    @classmethod
    def addNote(cls,reminder):
        cls.allReminders.append(reminder)
    @classmethod
    def showNotes(cls):
        return cls.allReminders
    @classmethod
    def searchNote(cls,searchTerm):
        allNotes = Notepad.showNotes()
        itemsFound = []
        for item in allNotes:
            searchTerm.replace(' ','')
            if(searchTerm in item.text):
                itemsFound.append(item)
                continue
            for tag in item.tags:
                if(searchTerm in tag):
                    itemsFound.append(item)
                    break
        return itemsFound
    @classmethod
    def modifyNote(cls,reminder):
        allNotes = Notepad.showNotes()
        for item in allNotes:
            if(str(item.id) == reminder.id):
                if reminder.text:
                    item.text = reminder.text 
                if reminder.tags:
                    item.tags = reminder.tags