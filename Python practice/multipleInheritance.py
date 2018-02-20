# Python example to show working of multiple 
# inheritance
class Base1(object):
	def __init__(self):
		self.str1 = "Geek1"
		print ("Base1")

class Base2(object):
	def __init__(self,str2):
		self.str2 = str2	
		print ("Base2")
	def printStrs1(self):
		print(self.str2)

class Derived(Base1, Base2):
	def __init__(self):
		
		# Calling constructors of Base1
		# and Base2 classes
		Base1.__init__(self)
		Base2.__init__(self,"greek2")
		print ("Derived")
		
	def printStrs(self):
		print(self.str1, self.str2)
		

#ob = Derived()
#ob.printStrs()
#ob.printStrs1()
class Person(object):
     
    # Constructor
    def __init__(self, name):
        self.name = name
 
    # To get name
    def getName(self):
        return self.name
 
    # To check if this person is employee
    def isEmployee(self):
        return False
 
 
# Inherited or Sub class (Note Person in bracket)
class Employee(Person):
 
    # Here we return true
    def isEmployee(self):
        return True
 
# Driver code
emp = Person("Geek1")  # An Object of Person
print(emp.getName(), emp.isEmployee())
 
emp = Employee("Geek2") # An Object of Employee
print(emp.getName(), emp.isEmployee())



