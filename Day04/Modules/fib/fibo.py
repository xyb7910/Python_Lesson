def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


def fibo(n):
    ans = []
    a, b = 0, 1
    while a < n:
        ans.append(a)
        a, b = a, a + b
    return ans
