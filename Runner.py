from AlbertCourse import *
from Scheduling import *
import os
import API_Request
import json
import datetime
#In testing

#Short Agenda:
#Switch to DateTime
#

def main():
    school = prompt_school()
    subject = prompt_subject(school)
    json_data = filter_json_data_by_code(school, subject, "1134")
    API_Request.print_format_json(json_data)
    lab_sections = get_section_from_json(json_data, "Lab")
    print(lab_sections)
    sample_test()
def prompt_school():
    all_schools = API_Request.get_school_list()
    return prompt_template(all_schools,"Pick a school: ","Bruhh")

def prompt_subject(school):
    all_subjects = API_Request.get_subject_list_by_school(school)
    return prompt_template(all_subjects, "Pick a subject: ", "Bruh")


def filter_json_data_by_code(school, subject, code, sem = "fa"):
    all_subjects = API_Request.get_courses(sem,school,subject)
    for i in all_subjects:
        if i["deptCourseId"] == code:
            return i

def get_section_from_json(json_data, section_type):
    all_sections = []
    for i in json_data["sections"]:
        if i["type"] == section_type:
            section_meetings = []
            if i["meetings"]:
                for meeting in i["meetings"]:
                    section_meetings.append(create_slot(meeting["beginDate"],meeting["minutesDuration"]))
            all_sections.append(section_meetings)
    return all_sections

def prompt_template(list,prompt,reject_response):
    reply = ""
    while reply not in list:
        print(prompt)
        print(*list, sep = ', ')
        reply = input()
        if reply not in list:
            print(reject_response)
    return reply

def convert_time(time, duration):
    start = datetime.datetime.strptime("2020-05-25 09:30:00", '%Y-%m-%d %X')
    end = start + datetime.timedelta(minutes = duration)
    print(end.weekday())

def create_slot(time, duration):
    start = datetime.datetime.strptime(time, '%Y-%m-%d %X')
    end = start + datetime.timedelta(minutes = duration)
    return (start.weekday(), start, end)

def sample_test():
    cs2124 = AlbertCourse("CS 2314")
    cs2124.add_lecture(create_slot("2020-05-25 09:30:00", 80),create_slot("2020-05-27 09:30:00", 80))
    cs2124.add_lecture(create_slot("2020-05-25 11:00:00", 80),create_slot("2020-05-27 11:00:00", 80))
    
    cs2124.add_lab(create_slot("2020-05-29 8:00:00",170))
    cs2124.add_lab(create_slot("2020-05-29 11:00:00",170))
    cs2124.add_lab(create_slot("2020-05-29 14:00:00",170))

    ma2314 = AlbertCourse("MA 2314")
    ma2314.add_lecture(create_slot("2020-05-25 09:30:00", 80),create_slot("2020-05-27 09:30:00", 80))
    ma2314.add_reci(create_slot("2020-05-28 10:00:00",50))
    ma2314.add_reci(create_slot("2020-05-28 11:00:00",50))
    ma2314.add_reci(create_slot("2020-05-28 14:00:00",50))
    ma2314.add_reci(create_slot("2020-05-28 15:00:00",50))

    exposua2 = AlbertCourse("EXPOS-UA 2")
    exposua2.add_lecture(create_slot("2020-05-26 08:00:00", 75),create_slot("2020-05-28 08:00:00", 75))

    cs1122 = AlbertCourse("CS 1122")
    cs1122.add_lab(create_slot("2020-05-29 09:00:00", 110))

    ph1013 = AlbertCourse("PH 1013")
    ph1013.add_lecture(create_slot("2020-05-25 15:30:00", 90),create_slot("2020-05-27 15:30:00", 90))
    ph1013.add_reci(create_slot("2020-05-29 14:00:00", 60))

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