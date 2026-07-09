students = []

while True:
    print("==============================")
    print(" STUDENT MANAGEMENT SYSTEM ")
    print("==============================")
    print("1. Add Student")
    print("2. View Students") 
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1": 
        name = input("Enter Student Name: ")
        students.append(name)
        print("Student Added Successfully!")

    elif choice == "2":
        print("Students List:")
        print(students)

    elif choice == "3":
        name = input("Enter Student Name to Delete: ")

        if name in students:
            students.remove(name)
            print("Student Deleted Successfully!")
        else:
            print("Student Not Found!")
    elif choice == "4":
        name = input("Enter Student Name to search: ")

        if name in students:
            print("Student Found!")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")


    
        