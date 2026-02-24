# list = ['apple', 'banana', 'orange', 'mango', 'peach'];
# max_list = ['shuaib', 25, True];
# print(list[:3])
# print(max_list)
# print(list[-4:-1])

# if 'orange' in list:
#     print("Orange is present")


# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:] = ["blackcurrant", "watermelon"]

# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# thislist.insert(0, "watermelon")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]

# thislist.extend(tropical);
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)


# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# # print(len(thislist))
# # for item in thislist:
# #     print(item)

# for item in range(len(thislist)):
#     print(thislist[item])


# thislist = ['apple', 'banana', 'cherry']
# i = 0
# while i < len(thislist):
#     print(thislist[i])
#     i += 1

# thislist = ['apple', 'banana', 'cherry']
# [print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if 'a' in x]
print(newlist)