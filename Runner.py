from AlbertCourse import *
from Scheduling import *
import os
import API_Request
#In testing
def main():
    all_subjects = API_Request.get_subjects()
    all_schools = [key for key in all_subjects.keys()]
    all_courses = {school:all_subjects[school] for school in all_schools}
    for entry in all_courses:
        print(entry,all_courses[entry])
    print()
    cs2124 = AlbertCourse("CS 2314")
    cs2124.add_lecture((0,9.50,10.83),(2,9.50,10.83))
    cs2124.add_lecture((0,11,12.33),(2,11,12.33))
    cs2124.add_lab((4,8,10.83))
    cs2124.add_lab((4,11,13.83))
    cs2124.add_lab((4,14,16.83))

    ma2314 = AlbertCourse("MA 2314")
    ma2314.add_lecture((0,9.50,10.83),(2,9.50,10.83))
    ma2314.add_reci((3,10,10.83))
    ma2314.add_reci((3,11,11.83))
    ma2314.add_reci((3,14,14.83))
    ma2314.add_reci((3,15,15.83))

    exposua2 = AlbertCourse("EXPOS-UA 2")
    exposua2.add_lecture((1,8,9.25),(3,8,9.25))

    cs1122 = AlbertCourse("CS 1122")
    cs1122.add_lab((4,9,10.83))

    ph1013 = AlbertCourse("PH 1013")
    ph1013.add_lecture((0,15.5,17),(2,15.5,17))
    ph1013.add_reci((4,14,15))

    sched = Scheduling(cs2124,ph1013,cs1122,exposua2,ma2314)
    sched.backtracking()
    i = 0
    n = len(sched.all_arrangements)
    if n == 0:
        print("Uh oh, your schedule seems impossible. Try adding more options or sth m8")
    else:
        while True:
            print("There are a total of %s arrangements. This is arrangement #%s" % (n,i+1))
            print(sched.all_arrangements[i])
            while True:
                string = input("D to see next schedule, A to see previous schedule, your mom hahaha to exit\n")
                if string.lower() == "d":
                    os.system('cls')
                    if i+1 < n:
                        i+=1
                    break
                if string.lower() == "a":
                    os.system('cls')
                    if i-1>-1:
                        i-=1
                    break
                if string.lower() == "your mom hahaha":
                    os.system('cls')
                    return
main()