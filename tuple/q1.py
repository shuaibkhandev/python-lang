# thistuple = ("apple", 'banana', 'cherry')
# print(thistuple[0])

# thistuple = ("apple",)
# print(type(thistuple))

# thistuple=("apple",2,True)
# print(thistuple)


# thistuple = ("apple", 'banana', 'cherry')
# convert_thistuple_tolist = list(thistuple)
# convert_thistuple_tolist[0] = "Apple";
# again_totuple = tuple(convert_thistuple_tolist)
# print(again_totuple, type(again_totuple))


# fruits = ("apple", "banana", "cherry")

# (green, *yellow) = fruits
# print(yellow)

# fruits = ("apple", "banana", "cherry")
# for fruit in fruits:
#     print(fruit)

# fruits = ("apple", "banana", "cherry")
# for x in range(len(fruits)):
#     print(fruits[x])

fruits = ("apple", "banana", "cherry", "apple")
print(fruits.count("apple"))
print(fruits.index("apple"))