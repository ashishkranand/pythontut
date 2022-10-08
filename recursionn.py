# def factorial_iterative(n):
#     fac =1
#     for i in range(n):
#         fac= fac*(i+1)
#     return fac
# number=int(input("Enter number:-->"))
# print(factorial_iterative(number))



# def factorial_recursive(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial_recursive(n-1)
# number=int(input("Enter number:-->"))
# print(factorial_recursive(number))


def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

num=int(input("Enter number till where you want to print fibonacci series:-->"))
print(fibonacci(num))



