print("Welcome to file5")

# def sum(a, b):
#     return a + b;

# res = sum(5,25)
# print(res)


# def isEven(num):
#     if(num%2 == 0):
#         print(num, "is even number")
#     else:
#         print(num, "is odd number")

# isEven(23);


# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
#     print("END")

# show(4);


def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)


res = factorial(5)
print(res)

