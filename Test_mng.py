from manager import StudentManager
manager= StudentManager()

manager.add_student("ali", 12, 23,5)
manager.add_student("syed", 34,55, 383)


print('\n Students' )
manager.view_students()

print('\n Search student' )
manager.search_student(5)

print('\n delete ' )
manager.delete_student(383)

print('\n Students' )
manager.view_students()






