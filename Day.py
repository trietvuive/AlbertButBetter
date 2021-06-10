from Classes import *
from SortedList import *
#This class represents each day of the week. Basically a wrapper for LinkedList
class Day:

    def __init__(self):
        self.day_interval = SortedList()

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