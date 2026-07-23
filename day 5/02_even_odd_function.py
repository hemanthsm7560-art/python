def check(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"


number = int(input("enter a number:"))
result = check(number)
print(result)
