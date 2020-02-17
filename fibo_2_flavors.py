# fibonaci series: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# fib(n) = fib(n-1) + fib(n-2)


# first in non recursive way (classical)
def fibo(n):
    if n == 1 or n == 2:
        return 1
    prev = 1
    prev_prev = 1

    for i in range(2, n):
        cur = prev + prev_prev
        prev_prev = prev
        prev = cur

    return cur

#let's do fibonaci recursive
def rec_fibo(n):
    if n == 1 or n == 2:
        return 1

    return rec_fibo(n-1) + rec_fibo(n-2)

print("the 10-th fibo is {}".format(fibo(10)))

print("the 10-th fibo is {}".format(rec_fibo(10)))