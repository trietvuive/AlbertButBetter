from Classes import *
from LinkedList import *
#object represents each day of the week
class Day:
    def __init__(self):
        self.day_interval = LinkedList()
    def insert_interval(self,start,end,name):
        self.day_interval.insert(start,end,name)
    def is_overlap(self,start,end):
        return self.day_interval.is_overlap(start,end)
    #iterate through every class in a day
    def __iter__(self):
        for i in self.day_interval:
            yield i
    def __str__(self):
        return str(self.day_interval)
    def copy(self):
        day = Day()
        for start,end,name in self.day_interval:
            day.insert_interval(start,end,name)
        return day