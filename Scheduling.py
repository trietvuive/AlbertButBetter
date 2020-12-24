from AlbertCourse import *
from WeekSchedule import *
#This class computes all possible schedule from a list of Albert courses
#All schedule are in the WeekSchedule format.
class Scheduling:
    def __init__(self,*all_courses):
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