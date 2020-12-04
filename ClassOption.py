from Day import Day
#object represents one option on Albert. Each option usually has 3 classes: lecture, recitation and lab 
class ClassOption:
    def __init__(self,lecture = None, reci = None, lab = None):
        self.days = []
        for i in range(5):
            self.days.append(Day())
        if lecture is not None:
            self.days[lecture.date].insert_class(lecture)
        if lab is not None:
            self.days[lab.date].insert_class(lab)
        if reci is not None:
            self.days[lab.date].insert_class(reci)