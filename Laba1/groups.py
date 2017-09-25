class Groups:

	def __init__(self):
		self.groups = []

	def add(self, group):
		self.groups.append(group)

	def remove(self, gid):
		for group in self.groups:
			if gid == group.gid:
				self.groups.remove(group)
				break

	def exist(self, gname):
		for group in self.groups:
			if gname == group.gname:
				return True
		return False
	
	def exist(self, gid):
		for group in self.groups:
			if gid == group.gid:
				return True
		return False

	#returns list of groups gid
	def get_gid_list(self):
		return [group.gid for group in self.groups]

	def __str__(self):
		return "\ngid\tgname\n---------------\n" + "\n".join(str(group) for group in self.groups)

	def max_gid(self):
		max_gid = 0
		for group in self.groups:
			if group.gid > max_gid:
				max_gid = group.gid
		return max_gid 		

