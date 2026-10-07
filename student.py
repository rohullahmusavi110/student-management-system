class Student:
    def __init__(self, name , age, marks, roll_no):
        self.name = name
        self.age= age
        self.marks= marks
        self.roll_no = roll_no


    def display_info(self):
        print(f"Name {self.name}")
        print(f"Age {self.age}")
        print(f"roll.No {self.roll_no}")
        print(f'Marks {self.marks}')
