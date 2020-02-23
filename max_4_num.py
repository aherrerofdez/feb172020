# Get number of inputs from user
while True:
    num = input("How many numbers do you want to write? ")
    try:
        num = int(num)
        break
    except:
        print("Invalid number")
        continue

numbers = []
count = 0
while True:
    if count >= num:
        break
    number = input("Enter a number: ")
    try:
        number = int(number)
    except:
        print("That was not a number")
        continue

    #We have a proper number
    numbers.append(number)
    count += 1

numbers.sort()
print("The maximum is {} ".format(numbers[num-1]))


