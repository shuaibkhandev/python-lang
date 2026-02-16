def print_kvargs(**kvargs):
    print(kvargs.items())
    for key , value in kvargs.items():
        print(key, value);
print_kvargs(name="Shuaib", age=25);