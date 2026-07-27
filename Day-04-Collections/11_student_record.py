name = input("Enter Student Name: ")
age = input("Enter Age: ")
marks = input("Enter Marks: ")

student = {
    "Name": name,
    "Age": age,
    "Marks": marks
}

with open("student.txt", "w") as file:
    for key, value in student.items():
        file.write(f"{key}: {value}\n")

print("\nStudent record saved successfully!\n")

with open("student.txt", "r") as file:
    print(file.read())
