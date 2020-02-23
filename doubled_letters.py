string = input("Enter text: ")

if string[::3] == string[1::3] == string[2::3]:
    print("All letters are tripled ")
else:
    print("Not all letters are tripled")

