from AlbertCourse import *
from WeekSchedule import *
class Scheduling:
    def __init__(self,all_courses):
        self.all_classes = []
        self.all_arrangements = []
        for i in all_courses:
            self.all_classes.append(i.lab_options)
            self.all_classes.append(i.reci_options)
            self.all_classes.append(i.lecture_options)
    def backtracking(self):
        def backtracking_helper(self,assignment,i):
            #print(str(i)+ " "+str(assignment))
            if i == len(self.all_classes):
                self.all_arrangements.append(assignment)
                return
            for classes in self.all_classes[i]:
                if not assignment.overlap_classes(classes):
                    assignment_copy = assignment.copy()
                    assignment_copy.insert_classes(classes)
                    backtracking_helper(self,assignment_copy,i+1)
            if(len(self.all_classes[i]) == 0):
                backtracking_helper(self,assignment,i+1)
        backtracking_helper(self,WeekSchedule(),0)


def main():

    cs2124 = AlbertCourse("CS 2314")
    cs2124.add_lecture([(0,9.50,10.83),(2,9.50,10.83)])
    cs2124.add_lecture([(0,11,12.33),(2,11,12.33)])
    cs2124.add_lab([(4,8,10.83)])
    cs2124.add_lab([(4,11,13.83)])
    cs2124.add_lab([(4,14,16.83)])

    ma2314 = AlbertCourse("MA 2314")
    ma2314.add_lecture([(0,9.50,10.83),(2,9.50,10.83)])
    ma2314.add_reci([(3,10,10.83)])
    ma2314.add_reci([(3,11,11.83)])
    ma2314.add_reci([(3,14,14.83)])
    ma2314.add_reci([(3,15,15.83)])

    exposua2 = AlbertCourse("EXPOS-UA 2")
    exposua2.add_lecture([(1,8,9.25),(3,8,9.25)])

    cs1122 = AlbertCourse("CS 1122")
    cs1122.add_lab([(4,9,10.83)])

    ph1013 = AlbertCourse("PH 1013")
    ph1013.add_lecture([(0,15.5,17),(2,15.5,17)])
    ph1013.add_reci([(4,14,15)])

    sched = Scheduling([cs2124,ph1013,cs1122,exposua2,ma2314])
    sched.backtracking()
    i = 0
    n = len(sched.all_arrangements)
    if n == 0:
        print("Uh oh, your schedule seems impossible. Try adding more options or sth m8")
    while True:
        print(sched.all_arrangements[i])
        while True:
            string = input("D to see next schedule, A to see previous schedule, X to exit\n")
            if string.lower() == "d":
                if i+1 < n:
                    i+=1
                    break
            if string.lower() == "a":
                if i-1>-1:
                    i-=1
                    break
            if string.lower() == "x":
                return
main()
