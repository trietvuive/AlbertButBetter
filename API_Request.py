import requests
import json

def get_data(url):
    response_obj = requests.get(url)

    if response_obj.status_code == 400:
        raise Exception("Path parameter(s) invalid")

    json_data = response_obj.json()
    return json_data
    

def print_format_json(json_data): #For testing and debugging purposes only
    print(json.dumps(json_data, indent = 2))
    


def get_schools():
    return get_data("https://schedge.a1liu.com/schools")
def get_school_list():
    return [school for school in get_schools().keys()]

def get_subjects():
    return get_data("https://schedge.a1liu.com/subjects")
def get_subject_list_by_school(school):
    return [subject for subject in get_subjects()[school].keys()]


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
            return

    if not valid:
        raise ValueError("Invalid Subject")

    

def get_courses(semester, school, subject, year = "current"):
    validate_sem_and_year(semester, year)

    url = "https://schedge.a1liu.com/" + str(year) + "/" + semester + "/" + school + "/" + subject
    return get_data(url)

def get_courses_by_school(semester, school, year):
    school = school.upper()
    validate_sem_and_year(semester, year)
    validate_school(school)

    url = "https://schedge.a1liu.com/" + str(year) + "/" + semester + "/search?query='" + school + "'&limit=9999&full=true"
    return get_data(url)

def get_courses_by_subject(semester, subject, year):
    subject = subject.upper()
    validate_sem_and_year(semester, year)
    validate_subject(subject)

    url = "https://schedge.a1liu.com/" + str(year) + "/"+ semester + "/search?query='" + subject + "'&limit=9999&full=true"
    return get_data(url)

def get_section(semester, registrationNumber, year):
    validate_sem_and_year(semester, year)

    if not isinstance(registrationNumber, int):
        raise TypeError("Registration Number must be of type int")
    
    url = "https://schedge.a1liu.com/" + str(year) + "/" + semester + "/" + str(registrationNumber)
    return get_data(url)
