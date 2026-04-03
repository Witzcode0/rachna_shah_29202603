
# nums = []

# print(dir(nums))

# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

# nums = [1,2,3,4,5]

# new_nums = [6,7,8,9,10]

# nums.append(new_nums)
# nums.extend(new_nums)
# nums.insert(1, new_nums)
# nums.pop(2)
# print(nums)

# num1 = 10
# num2 = 10
# num1 = []
# num2 = []
# num2 = num1.copy()
# print(id(num1), id(num2))

# nums = [1,2,2,1,3,1,1,2,1,34]

# print(set(nums))

# contact = {3}
# print(type(contact))

contact = {
    "A" : [
        {
            "Aman": {
                "Mobile": ['675476547', '84765837'],
                "Email" : "aman@gmail.com"
            }
        },
        {
            "Ajay": {
                "Mobile": ['84765837567'],
                "Email" : "ajay@gmail.com"
            }
        }
    ]
}

#  '', '', 'fromkeys', '', '', '', '', '', 'setdefault', 'update', ''

# print(dir(contact))

# print(contact.keys())
# print(contact.values())
# print(contact.items())

# items = ["potato", "tomato", "onion"]
# price = 50

# pro = dict()
# pro.fromkeys(items, price)
# print(pro.fromkeys(items, price))

# car = {
#     # "color" : "Blue"
# }

# car.setdefault("color", "black")
# print(car)


car = {
    "color" : "Blue"
}

new_data = {
    "model": "xyz",
    "color": "Black"
}

car.update(new_data)

print(car)