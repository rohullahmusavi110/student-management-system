
from storage import save_students, load_students
from student import Student


class StudentManager:
   def __init__(self):
    self.students = load_students()

   def add_student(self, name, age, marks, roll_no):
    student = Student(name, age, marks, roll_no)
    self.students.append(student)

    save_students(self.students)

    print("Student added successfully!")
    def view_students(self):
        if not self.students:
            print("No students found.")
            return

        for student in self.students:
            student.display_info()
            print("----------------")

    def search_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                student.display_info()
                return

        print("Student not found.")

    def delete_student(self, roll_no):
       
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)


                save_students(self.students)

                print("Student deleted successfully!")

                return
            

            print("Student not found.")

            