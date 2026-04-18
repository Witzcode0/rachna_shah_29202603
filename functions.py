# def function_name(paras):
#     code of block

# function_name(values)

# def add(a,b,c):
#     print(a + b + c)

# add(10, 20, 30)

# Positional para
# def add(a,b,c):
#     return a + b + c

# print(add(10, 20, 30))

# def bill(fees, dis=5, tomato=50):
#     print(tomato + fees)

# bill(5, 10, 45)

# variable length:
# *args
# **kwargs

# def add(a,b,c, d):
#     print(a + b + c + d)

# def add(*nums):
#     print(sum(nums))

# add(10,20,30,40,50, 60)

# def bill(**items):
#     print(sum(items.values()))

# bill(onion=50, tomato=20)

# add = lambda num1, num2: num1 + num2
# print(add(10, 20))


# nums = [1,2,3,4,5,6,7,8,9,10]

# print(list(filter(lambda num: num % 2 == 0, nums)))
# print(list(filter(lambda num: num % 2 != 0, nums)))
# print(list(map(lambda num: num * 2 , nums)))


# var = 10 # Global

# def test():
#     global var
#     # print(id(var))
#     var = 20 # Local
#     # print(id(var))
#     print(var)

# print(var)
# test()
# print(var)

# num1 = 10
# num2 = 10
# print()

# -------------------------------------------------
# def title_case(func):
#     print(func())
#     def wrap():
#         res = func()
#         print("title case: ", res)
#     return wrap

# @title_case
# def text(word):
#     print(word)

# text(input("enter something: "))
# ----------------------------------------------


# def title_case(func):
#     def wrapper():
#         res = func()
#         print("title case: ", res)
#     return wrapper

# @title_case
# def text(word):
#     print("User input: ", word)
#     return word

# # text(input("Enter something: "))
# text("BhARaT FUturiST AI")


# -----------------------------------------

# def title_case(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__} with {args}")
#         print(args[0].title())
#         return func(*args, **kwargs)
#     return wrapper

# def upper_case(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__} with {args}")
#         print(args[0].upper())
#         return func(*args, **kwargs)
#     return wrapper

# @title_case
# @upper_case
# def text(a):
#     return a

# print(text("BhARaT FUturiST AI"))

# def outer():
#     print("I am from outer")
#     def inner():
#         print("I am from inner")
#     return inner()

# outer()