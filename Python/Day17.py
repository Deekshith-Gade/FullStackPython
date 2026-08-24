
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fact(n-1)
n=int(input())
print(fact(n))


def fib(a):
    if a==0:
        return 0
    elif a==1:
        return 1
    else:
        return fib(a-2)+fib(a-1)
a=int(input())
print(fib(a))