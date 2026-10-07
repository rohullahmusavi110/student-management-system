
from manager import StudentManager


def main():
    manager = StudentManager()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            marks = float(input("Enter marks: "))
            roll_no = input("Enter roll number: ")

            manager.add_student(name, age, marks, roll_no)

        elif choice == "2":
            manager.view_students()

        elif choice == "3":
            roll_no = input("Enter roll number: ")
            manager.search_student(roll_no)

        elif choice == "4":
            roll_no = input("Enter roll number: ")
            manager.delete_student(roll_no)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()