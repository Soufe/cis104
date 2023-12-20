class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return f"My name is {self.firstname} {self.lastname}"

class Student(Person):
    def __init__(self, firstname, lastname, student_id):
        super().__init__(firstname, lastname)
        self.student_id = student_id

    def __str__(self):
        return super().__str__() + f" [{self.student_id}]"

class Teacher(Person):
    def __init__(self, firstname, lastname, email):
        super().__init__(firstname, lastname)
        self.email = email

    def __str__(self):
        return super().__str__() + f" {self.email}"