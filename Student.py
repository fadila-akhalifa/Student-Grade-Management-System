class student:
    def __init__(self, name, student_id , grade):
        self.name = name 
        self.student_id = student_id
        self.grade = grade 

    def display_info(self):
        print("Student Name:", self.name)
        print("Student ID:", self.student_id)
        print("Grades:", self.grade)

class UndergraduateStudent(student):
    def __init__(self,name,student_id, grade ,major):
      super().__init__(name, student_id , grade)
      self.major = major

    def display_info(self):
      super().display_info()
      print(f"Major: {self.major}")

class GraduateStudent(student):
    def __init__(self,name, student_id ,grade , program_title):
      super().__init__(name , student_id , grade)
      self.program_title = program_title
  
    def display_info(self):
      super().display_info()
      print(f"Program title:{self.program_title}")



