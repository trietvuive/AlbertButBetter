class AlbertCourse:
	def __init__(self,course_options = []):
		self.course_options = course_options
	def add_option(self,option):
		self.course_options.append(option)