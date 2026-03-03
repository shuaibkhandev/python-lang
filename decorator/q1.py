# def changecase(func):
#     def inner():
#         return func().upper()
#     return inner

# @changecase
# def myfunction():
#     return "Hello Shuaib"

# print(myfunction())


# def changecase(func):
#     def inner(x):
#         return func(x).upper()
#     return inner

# @changecase
# def myfunction(name):
#     return f"Hello {name}"

# print(myfunction("Shuaib"))
# print(myfunction("Asad"))


# def changecase(func):
#     def inner(*args, **kwargs):
#         return func(*args, **kwargs).upper()
#     return inner

# @changecase
# def myfunction(name):
#     return f"Hello {name}"

# print(myfunction("Shuaib"))
# print(myfunction("Asad"))

def changecase(n):
    def changecase(func):
        def inner():
            if n == 1:
                a = func().lower()
            else:
                a = func().upper()
            return a
        return inner
    return changecase
                
@changecase(2)
def myFunc():
    return "Hello Shuaib"
print(myFunc())