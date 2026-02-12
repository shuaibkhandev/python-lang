user_age = int(input("Please enter your age: "));

if user_age < 13:
    print("You'r Child.");
elif user_age < 20:
    print("You'r Teenager.");
elif user_age < 60:
    print("You'r Adult.");
else:
    print("You'r Senior.")