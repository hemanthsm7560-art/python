num = int(input("enter a number:"))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("is not prime")
            break
        else:
            print("is prime")
    else:
        print("not prime")
