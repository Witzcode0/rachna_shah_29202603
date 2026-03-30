# name = "Python"

# for n in name:
#     print(n)

# code = "python"

# i = iter(code)

# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# *
# * *
# * * *
# * * * *
# * * * * *

# num = 5
# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print("*", end="")
#     print()

num = 5
for row in range(1, num+1):
    print("*"*row)

#         * 4 + 1
#       * * 3 + 2
#     * * * 2 + 3
#   * * * * 1 + 4
# * * * * * 0 + 5


# num = 5
# for row in range(1, num+1):
#     for col in range(1, num-row+1):
#         print("-", end=" ")
#     for col in range(1, row+1):
#         print("*", end=" ")
#     print()

# num = 5
# for row in range(1, num+1):
#     print(" "*(num-row), f" {chr(row+64)}"*row)