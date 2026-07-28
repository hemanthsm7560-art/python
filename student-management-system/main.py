class Student:
    def __init__(self, roll, name, age, course):
        self.roll = roll
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("-" * 40)
        print("Roll No :", self.roll)
        print("Name    :", self.name)
        print("Age     :", self.age)
        print("Course  :", self.course)
        print("-" * 40)

    def to_record(self):
        return f"{self.roll},{self.name},{self.age},{self.course}\n"


students = []

# Load existing students from file if it exists
try:
    with open("students.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue

            data = line.split(",")
            if len(data) != 4:
                print("Invalid record:", repr(line))
                continue

            roll, name, age, course = data
            student = Student(roll, name, age, course)
            students.append(student)
except FileNotFoundError:
    # No existing file; start with empty list
    pass


while True:

    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # ---------------- ADD ----------------
    if choice == "1":

        roll = input("Enter Roll Number : ")
        name = input("Enter Name        : ")
        age = input("Enter Age         : ")
        course = input("Enter Course      : ")

        student = Student(roll, name, age, course)

        students.append(student)

        with open("students.txt", "a") as file:
            file.write(student.to_record())

        print("\n✅ Student Added Successfully!")

    # ---------------- VIEW ----------------
    elif choice == "2":

        if len(students) == 0:
            print("\nNo students found.")

        else:
            print("\nStudent Records\n")

            for student in students:
                student.display()

    # ---------------- SEARCH ----------------
    elif choice == "3":

        roll = input("Enter Roll Number to Search: ")

        found = False

        for student in students:
            if student.roll == roll:
                print("\nStudent Found\n")
                student.display()
                found = True
                break

        if not found:
            print("\nStudent Not Found.")

    # ---------------- DELETE ----------------
    elif choice == "4":

        roll = input("Enter Roll Number to Delete: ")

        found = False

        for student in students:
            if student.roll == roll:
                students.remove(student)
                found = True
                break

        if found:

            with open("students.txt", "w") as file:
                for student in students:
                    file.write(student.to_record())

            print("\n✅ Student Deleted Successfully!")

        else:
            print("\nStudent Not Found.")

    # ---------------- EXIT ----------------
    elif choice == "5":

        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice! Try Again.")
