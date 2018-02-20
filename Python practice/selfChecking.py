class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self1, name, salary1):
      self1.name = name
      self1.salary = salary1
      Employee.empCount += 1
   
   def displayCount(self1):
     test=100
     print (test)

   def displayEmployee(self1):
      print ("Name : ", self1.name,  ", Salary: ", self1.salary)

emp1 = Employee("Ashok", 2000)
emp2 = Employee("Naveen", 5000)
emp3 = Employee("Naveen2", 5000)
emp4 = Employee("Naveen3", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
emp1.displayCount()

