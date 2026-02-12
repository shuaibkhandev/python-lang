# user_age = int(input("Please enter your age: "));
# sale_day = "monday";
# if user_age < 18:
#     if sale_day == "wednesday":
#         print("your ticket price is $6")
#     else:
#         print("your ticket price is $8");
# else:
#     if sale_day == "wednesday":
#         print("your ticket price is $10");
#     else:
#         print("Your ticket price is $12");
    

user_age = int(input("Please enter your age: "));
day = "wednesday";

price = 12 if user_age >= 18 else 8;

if day == "wednesday":
    price -= 2;
    print("your ticket price is $", price);
else:
    print("your ticket price is $", price);