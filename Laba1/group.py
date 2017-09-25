class Group:

	def __init__(self, gid, gname):
		self.gid = gid
		self.gname = gname

	def __str__(self):
		return " %d\t%s" % (self.gid, self.gname)