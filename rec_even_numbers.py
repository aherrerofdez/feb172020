def even(n):
    if n == 1:
        return 2

    return even(n - 1) + 2


print(even(20))


def factorial(n):
    # 0! = 1
    if n == 0:
        return 1
    # Factorial formula: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)


print(factorial(20))