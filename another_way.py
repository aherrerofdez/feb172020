my_numbers = input("Please give me 4 numbers, separated by ,")

list_numbers = my_numbers.split(", ")
# print(list_numbers)

numbers = []
for i in list_numbers:
    try:
        numbers.append(int(i))
    except:
        print("that was not a number")

numbers.sort()
print(numbers)
