import pickle
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
        allNotes = cls.showNotes()
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
        allNotes = cls.showNotes()
        for item in allNotes:
            if(str(item.id) == reminder.id):
                if reminder.text:
                    item.text = reminder.text 
                if reminder.tags:
                    item.tags = reminder.tags
    @classmethod
    def exportNote(cls,name):
        allNotes = cls.showNotes()
        pickle.dump( allNotes , open( name + ".rmdr", "wb" ) )
    @classmethod
    def importName(cls,name):
        try:
            importedNotes = pickle.load( open( name, "rb" ))
            cls.addImportedNote(importedNotes)
        except:
            print("There was an error reading the file!")
    @classmethod
    def addImportedNote(cls,importedReminders):
        allNotes = cls.showNotes()
        for item in importedReminders:
            if(cls.idExists(item.id)):
                #Handle same id's situation
                print("Duplicated ID")
            else:
                allNotes.append(item)
    @classmethod
    def idExists(cls,id):
        allNotes = cls.showNotes()
        isFound = False 
        for item in allNotes:
            if(item.id == id):
                isFound = True
                break
        return isFound