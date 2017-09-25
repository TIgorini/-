from student import Student
from students import Students
from group import Group
from groups import Groups
import pickle


def add_g():
	gname = raw_input("Enter group name: ")
	if not groups.exist(gname):
		groups.add(Group(groups.max_gid() + 1, gname))
		print("Group \"" + gname + "\" added")
	else:
		print("This group is already exist")

def add_s():
	name = raw_input("Enter student name: ")
	try:
		gid = input("Enter gid: ")
		if not groups.exist(gid):
			print("No such group")
			return
		age = input("Enter age: ")
	except:
		print("Incorrect data")
		return
	students.add(Student(students.max_sid() + 1, gid, name, age))
	print("Student \"" + name + "\" added")

def remove_g():
	try:
		print("This operetion also will remove all students in this group !!!")
		gid = input("Enter removing gid: ")
	except:
		print("Incorrect data")
		return

	if not groups.exist(gid):
		print("No such group")
	else:
		for sid in students.get_list_by_gid(gid):
			students.remove(sid)
			print("Student with sid: \"" + str(sid) + "\" removed")
		groups.remove(gid)
		print("Group with gid: \"" + str(gid) + "\" removed")

def remove_s():
	try:
		sid = input("Enter removing sid: ")
	except:
		print("Incorrect data")
		return

	if students.exist(sid):
		students.remove(sid)
		print("Student with sid: \"" + str(sid) + "\" removed")
	else:
		print("No such student")
		
def list_g():
	print(groups)

def list_s():
	print(students)

#prints list with the youngest students in each group
def filtr():
	print("\nsid\tgid\tage\tname\n------------------------------------------")
	for gid in groups.get_gid_list():
		for stud in students.youngest(gid):
			print(stud)

#reading from files
try:
	with open("groups.obj","rb") as gfile:
		groups = pickle.load(gfile)
except IOError:
	groups = Groups()

try:
	with open("students.obj","rb") as sfile:
		students = pickle.load(sfile)
except IOError:
	 students = Students()


#UI realisation
commands = {11: add_g, 12: add_s, 21: remove_g, 22: remove_s, 31: list_g, 32: list_s, 4: filtr}
while True:
	try:
		comm = str(input("\n1. Add\n2. Remove\n3. List\n4. Filter\n0. Done\nEnter command: "))
		if comm == '1' or comm == '2':
			comm += str(input("\n1. Group\n2. Student\n0. Back\nEnter command: "))
			if comm == '10' or comm == '20':
				continue
		elif comm == '3':
			comm += str(input("\n1. Groups\n2. Students\n0. Back\nEnter command: "))
			if comm == '30':
				continue
		elif comm == '0':
			break
	except:	
		print("Incorrect command")
		continue
	commands[int(comm)]()


#writing to files
with open("groups.obj","wb") as gfile:
	pickle.dump(groups, gfile)

with open("students.obj","wb") as sfile:
	pickle.dump(students, sfile)