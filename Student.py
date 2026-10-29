class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.__grade = []

    def get_grades(self):
        return self.__grade.copy()

    def add_grades(self, grade):
        if isinstance(grade, (int, float)) and 0 <= grade <= 100:
            self.__grade.append(grade)
        else:
            print("Invalid grade!")

    def calculate_average(self):
        if len(self.__grade) == 0:
            return 0
        return sum(self.__grade) / len(self.__grade)

    def calculate_grade(self):
        if len(self.__grade) == 0:
            return "N/A"
        average = self.calculate_average()
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Grades: {self.get_grades()}")
        print(f"Average Grade: {self.calculate_average()}")
        print(f"Letter Grade: {self.calculate_grade()}")

class UndergraduateStudent(Student):
    def __init__(self,name,student_id, grade ,major):
      super().__init__(name, student_id , grade)
      self.major = major

    def display_info(self):
      super().display_info()
      print(f"Major: {self.major}")

class GraduateStudent(Student):
    def __init__(self,name, student_id ,grade , program_title):
      super().__init__(name , student_id , grade)
      self.program_title = program_title
  
    def display_info(self):
      super().display_info()
      print(f"Program title:{self.program_title}")



