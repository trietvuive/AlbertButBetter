from Day import Day
from Classes import Classes
#This class represents a 5-day schedule (basically a class that contains 5 instances of Day as well as all the methods)
class WeekSchedule:

    def __init__(self):
        self.week = []
        for i in range(5):
            self.week.append(Day())

    def overlap_classes(self,classes):
        overlap = False
        for date,start,end in classes.timeslot:
            if date<5:
                overlap |= self.week[date].is_overlap(start,end)
            else:
                overlap = True
        return overlap

    def insert_classes(self,classes):
        for date,start,end in classes.timeslot:
            if date<5:
                self.week[date].insert_interval(start,end,classes.name)

    def __str__(self):
        ret = ""
        week = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
        for i in range(5):
            ret+= week[i]+": "+str(self.week[i])
            ret+="\n"
        return ret

    def copy(self):
        sched = WeekSchedule()
        for i in range(5):
            sched.week[i] = self.week[i].copy()
        return sched
