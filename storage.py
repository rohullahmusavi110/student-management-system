import json
from student import Student
FILE_NAME = "students.json"


def save_students(students):
    Data =[]

    for student in students:
        Data.append({
            "name": student.name,
            "age": student.age,
            "marks": student.marks,
            "roll_No": student.roll_no
            })

        with open(FILE_NAME, "w") as file:
            json.dump(Data, file, indent=4)
            print("Data saved successfully.")


def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            Data=json.load(file)

            students=[]

            for item in Data:
                student=student(
                    item["name"],
                    item["age"],
                    item["marks"],
                    item["roll_no"]
                )
                students.append(student)

                return students
    except FileNotFoundError:
        return[]

