#object represent either lecture, lab, or recitation. One class, one date, start and end at certain time
class OneClass:
    def __init__(self,date,start,end,course):
        self.date = date
        self.start = start
        self.end = end
        self.course = course