import requests
import json

from datetime import date

def get_data(url):
    response_obj = requests.get(url)

    if response_obj.status_code == 404:
        raise Exception("Resource cannot be found")

    json_data = response_obj.json()
    return json_data
    

def print_format_json(json_data): #For testing and debugging purposes only
    print(json.dumps(json_data, indent = 2))
    


def get_schools():
    return get_data("https://schedge.a1liu.com/schools")

def get_subjects():
    return get_data("https://schedge.a1liu.com/subjects")

def validate_sem_and_year(semester, year):
    valid_sem = ["su", "sp", "fa", "ja"]
    
    if semester not in valid_sem:
        raise ValueError("Invalid Semester")

    if not (year == "current" or isinstance(year, int)):
        raise ValueError("Invalid Year")

def validate_school(school): 
    if school not in get_schools():
        raise ValueError("Invalid School")

def validate_subject(subject):
    valid = False
    subjects = get_subjects()
    
    for school in get_schools():
        school_subjects = subjects.get(school)
        
        if school_subjects is not None and subject in school_subjects:
            valid = True
            break

    if not valid:
        raise ValueError("Invalid Subject")

    

def get_courses(semester, school, subject, year = "current"):
    validate_sem_and_year(semester, year)

    url = "https://schedge.a1liu.com/" + str(year) + "/" + semester + "/" + school + "/" + subject
    return get_data(url)

def get_courses_by_school(semester, school, year = "current"):
    school = school.upper()
    validate_sem_and_year(semester, year)
    validate_school(school)

    if year == "current":
        year = date.today().year

    url = "https://schedge.a1liu.com/" + str(year) + "/fa/search?query='" + school + "'&limit=9999"
    return get_data(url)

def get_courses_by_subject(semester, subject, year = "current"):
    subject = subject.upper()
    validate_sem_and_year(semester, year)
    validate_subject(subject)

    if year == "current":
        year = date.today().year

    url = "https://schedge.a1liu.com/" + str(year) + "/fa/search?query='" + subject + "'&limit=9999"
    return get_data(url)
