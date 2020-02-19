class Reminder:
    _numberOfReminder = 0
    def __init__(self, text,  tags = []):
        self.text = text
        self.tags = tags
        self.id = Reminder._numberOfReminder + 1
        Reminder._numberOfReminder += 1