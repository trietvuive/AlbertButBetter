from OneClass import *
from LinkedList import *
class Day:
    def __init__(self):
        self.day_interval = LinkedList()
    def insert_interval(self,start,end):
        return self.day_interval.insert(start,end)
    def insert_option(self,option):
        return self.insert_interval(option.start,option.end)
    def is_overlap(self,option):
        return self.day_interval.is_overlap(option.start,option.end)
    #iterate through every class in a day
    def __iter__(self):
        for i in self.day_interval:
            yield i
thursday = Day()
print(thursday.insert_interval(1,3))
print(thursday.insert_interval(4,6))

print(thursday.insert_interval(-1,0))
eg1003 = OneClass(1,5,7,"EG 1003")
print(thursday.is_overlap(eg1003))
print(thursday.insert_option(eg1003))
for i in thursday:
    print(i)

