import random
numbers = []
for i in range(100):
    numbers.append(random.randint(0,1000))

print("original values {}".format(numbers))

def merge(numbers):
    if len(numbers) == 1:
        return numbers
    middle = len(numbers)//2
    left = numbers[0: middle]
    right = numbers[middle:]

    #sort these 2 halves
    left = merge(left)
    right = merge(right)

    merged = []
    #now they are sorted and need to merge them
    i = 0 #for left
    j = 0 # for right
    k = 0 #for merged
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
        k += 1
    while i < len(left):
        merged.append(left[i])
        i += 1
        k += 1

    while j < len(right):
        merged.append(right[j])
        j += 1
        k += 1
    return merged

sorted = merge(numbers)
print(sorted)