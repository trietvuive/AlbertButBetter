#sortedlist used to efficiently represent each date
#Use to detect overlap and adding in O(n)
#Another possible implementation would be to use a bunch of bits, which would detect overlap in O(1) by doing & operation
from bisect import *
class SortedList:

    def __init__(self):
        self.events = []

    def insert(self,start,end,name):
        if start>=end:
            return False
        i = bisect_left(self.events,(start,end,name))
        if (i-1>=0 and self.events[i-1][1]>=start) or (i!=len(self.events) and self.events[i][0]<=end):
            return False
        self.events.insert(i,(start,end,name))
        return True
    def is_overlap(self,start,end):
        if start>=end:
            return False
        i = bisect_left(self.events,(start,end,""))
        if (i-1>=0 and self.events[i-1][1]>=start) or (i!=len(self.events) and self.events[i][0]<=end):
            return True
        return False
    def __iter__(self):
        for i in self.events:
            yield i

    def __str__(self):
        return str.join(", ",[str(i[2])+ ": "+str(i[0])+"->"+str(i[1]) for i in self])
