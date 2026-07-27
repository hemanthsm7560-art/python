while True:

    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        name = input("Enter student name: ")

        file = open("students.txt", "a")
        file.write(name + "\n")
        file.close()

        print("Student Added Successfully.")

    elif choice == "2":

        try:
            file = open("students.txt", "r")
            print("\nStudents List")
            print("----------------")

            print(file.read())

            file.close()

        except FileNotFoundError:
            print("No student records found.")

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
