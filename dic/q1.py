# print("HELLO WORLD")

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict['brand'] = "Ford 2"
# thisdict.popitem()
# print(thisdict)

# for key in thisdict:
#     print(key, ":", thisdict[key])


myfamily = {
    "child1" : {
        "name": "Emil",
        "year": 2004 
    },
    "child2" : {
        "name" : "Tobias",
        "year": 2007
    }
}

# print(myfamily["child2"]["name"])

for key, val in myfamily.items():
    print(key)
    for inner_key in val:
        print(inner_key, val[inner_key])