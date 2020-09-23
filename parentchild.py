#Parent Class User
class User:
    name = "Jay"
    email = "Krom"
    password = "1234abcd"

    def getLoginInfo(self):
        entry_name= input("Type name: ")
        entry_email = input("Type email: ")
        entry_password = input("Type password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Hello, {}".format(entry_name))
        else:
            print("Incorrect")

#Child Class Student
class Student(User):
    grade = "Freshman"
    age = 14

    def getLoginInfo(self):
        entry_name= input("Type name: ")
        entry_email = input("Type email: ")
        entry_pin = input("Type pin: ")
        if (entry_email == self.email and entry_pin == self.pin):
            print("Hello, {}".format(entry_name))
        else:
            print("Incorrect")

class Teacher(User):
    room_numb: 210
    salary: 40k
    
    def getLoginInfo(self):
        entry_name= input("Type name: ")
        entry_email = input("Type email: ")
        entry_code = input("Type code: ")
        if (entry_email == self.email and entry_code == self.code):
            print("Hello, {}".format(entry_name))
        else:
            print("Incorrect")

parent = User()
parent.getLoginInfo()

student = Student()
student.getLoginInfo()

principal = Teacher()
principal.getLoginInfo()
