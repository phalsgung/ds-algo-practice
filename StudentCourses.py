lists =[]
# print(dir(lists))
lists.extend([1, "abc"])
# print(lists)


# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


class Student:
	
	def __init__(self, name):
		self.Name = name

	def __repr__(self):
		return "Student: " + self.Name

	def __hash__(self):
		return hash((self.Name))

	def __eq__(self, item):
		print("item: ")
		print(item)
		return True

	def getName(self):
		return self.Name


class Course:

	def __init__(self, name):
		self.Name = name
		self.StudentSet = set()

	def addStudent(self, Student):
		self.StudentSet.add(Student)

	def getStudentList(self):
		return self.StudentSet

# Name = input("Enter Student Name: ")
S1 = Student("Phals")

# Name = input("Enter Student Name: ")
S2 = Student("Phals")

# Name = input("Enter Course Name: ")
C1 = Course("Maths")

C1.addStudent(S1)
C1.addStudent(S2)

print(C1.getStudentList())

