first_time = []
second_time = []
with open("text.txt") as f:
    for line in f:
        words = line.split()
        for word in words:
            if word in first_time:
                if word in second_time:
                    # nothing to do
                    pass
                else:
                    # we have found the second occurrence
                    second_time.append(word)
            else:
                # first occurrence
                first_time.append(word)

print(second_time)
