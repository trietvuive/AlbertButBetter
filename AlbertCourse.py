#Albert allows students to choose lectures from a list of possible lecture
#reci from a list of possible reci and lab from a list of possible lab to form their schedule
from Classes import Classes
#This class represents 
class AlbertCourse:

	def __init__(self,name):
		self.name = name
		self.lab_options = []
		self.reci_options = []
		self.lecture_options = []

	def add_lab(self,*all_slots):
		lab = Classes(self.name)
		for date,start,end in all_slots:
			lab.insert_slot(date,start,end)
		self.lab_options.append(lab)

	def add_reci(self,*all_slots):
		reci = Classes(self.name)
		for date,start,end in all_slots:
			reci.insert_slot(date,start,end)
		self.reci_options.append(reci)

	def add_lecture(self,*all_slots):
		lecture = Classes(self.name)
		for date,start,end in all_slots:
			lecture.insert_slot(date,start,end)
		self.lecture_options.append(lecture)