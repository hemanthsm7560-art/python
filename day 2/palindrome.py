num = int(input("enter a number: "))
num_str = str(num)

if num_str == num_str[::-1]:
    print("palindrome")
else:
    print("not palindrome")
