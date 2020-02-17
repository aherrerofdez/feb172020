def even(n):
    if n==1:
        return 2

    return even(n-1) + 2

print(even(20))