class Students:

	def __init__(self):
		self.students = []

	def add(self, student):
		self.students.append(student)

	def remove(self, sid):
		for student in self.students:
			if sid == student.sid:
				self.students.remove(student)
				break

	#returns list with sid`s that belong to given gid  			
	def get_list_by_gid(self, gid):
		return [student.sid for student in self.students if gid == student.gid]

	def exist(self, sid):
		for student in self.students:
			if sid == student.sid:
				return True
		return False 

	def youngest(self, gid):
		min_age = 0
		for student in self.students:
			if student.gid == gid:
				min_age = student.age
				break

		if min_age == 0:
			return []

		for student in self.students:
			if student.gid == gid and min_age > student.age:
				min_age = student.age
		return [student for student in self.students if student.age == min_age and student.gid == gid]


	def __str__(self):
		return "\nsid\tgid\tage\tname\n------------------------------------------\n" + "\n".join(str(stud) for stud in self.students)

	def max_sid(self):
		max_sid = 0
		for student in self.students:
			if student.sid > max_sid:
				max_sid = student.sid
		return max_sid