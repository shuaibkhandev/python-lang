password = input("please Enter Your password: ");

if len(password) >= 10:
    print("Strong Password");
elif len(password) >= 6:
    print("Medium Password");
else:
    print("Weak Password"); 