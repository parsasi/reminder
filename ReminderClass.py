class Reminder:
    numberOfReminder = 0
    def __init__(self, text,  tags = []):
        self.text = text
        self.tags = tags
        self.id = Reminder.numberOfReminder + 1
        Reminder.numberOfReminder += 1