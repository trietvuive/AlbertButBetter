#lecture, lab, and reci can take up more than 1 timeslot.
class Classes:

    def __init__(self,name):
        self.name = name
        self.timeslot = []

    def insert_slot(self,date,start,end):
        self.timeslot.append((date,start,end))