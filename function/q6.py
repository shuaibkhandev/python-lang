def coundown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        coundown(n-1)

coundown(3)