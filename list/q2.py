# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if 'a' in x]
# newlist2 = [x for x in fruits if x != 'apple']
# print(newlist2)


mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print(mylist)

mylist = ['apple', 'banana', 'cherry']
mylist.insert(0, 'orange')
print(mylist)