from AlbertCourse import *
from WeekSchedule import *
from Day import *
from Classes import *
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
    cs2124.add_lab([(1,8,11),(1,12,15)])
    cs2124.add_lecture([(4,12,13.5),(4,14,16)])
    ma2314 = AlbertCourse("MA 2314")
    ma2314.add_lab([(3,8,11),(3,12,15)])
    all_courses = [cs2124,ma2314]
    sched = Scheduling(all_courses)
    sched.backtracking()
    for i in sched.all_arrangements:
        print(i)
main()
