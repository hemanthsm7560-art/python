def calculator(a, b):
    print("addition:", a + b)
    print("subtraction:", a - b)
    print("multiplication:", a * b)
    if b != 0:
        print("division:", a / b)
    else:
        print("cannot divide by zero")


calculator(5, 6)
