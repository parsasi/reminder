import Reminder
allReminders = []
def printMenu():
    print("Menu:\n\t1. Show all reminders\n\t2. Search all reminders\n\t3. Add reminders\n\t4. Modify reminders\n\t5. Export reminders\n\t6. Import reminders\n\t7. Exit\nYour Choice:\t")
    return input()
q = False
while(q == False):
    command = printMenu()
    q = (command == "7")  
    if(q):break
    if(command == "1"):
        print(command)
    elif(command == "2"):
        print(command)
    elif(command == "3"):
        print(command)
    elif(command == "4"):
        print(command)
    elif(command == "5"):
        print(command)
    elif(command == "6"):
        print(command)
    else:
        continue
