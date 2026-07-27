num = int(input("enter a number:"))
if num <= 1:
    print("not prime")
else:
    is_prime = True

for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        is_prime = False
        break

if is_prime == True:
    print("prime")
else:
    print("not prime")
