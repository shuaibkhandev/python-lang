def sum_all(*args):
    print(args)
    for num in args:
        print(num)
    return sum(args);

print(sum_all(1,2,3))