try:
    file = open("abc.txt", "r")
    file.read()
except FileNotFoundError:
    print("file not found")
