#PROGRAM 12
def factorial(n):
    return (1 if (n == 1 or n == 0) else n * factorial(n - 1))


n = int(input("enter number: "))
print("factorial of {} is: {}".format(n , factorial(n)))
