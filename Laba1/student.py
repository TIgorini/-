class Student:

	def __init__(self, sid, gid, name, age):
		self.gid = gid
		self.sid = sid
		self.name = name
		self.age = age

	def __str__(self):
		return " %d\t%d\t%d\t%s" % (self.sid, self.gid, self.age, self.name)