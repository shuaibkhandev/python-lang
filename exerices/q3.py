# std_numbers = int(input("Enter Your Numbers: "));

# if std_numbers <= 100 and std_numbers >= 90:    
#     print("Your Grade is A");
# elif std_numbers < 90 and std_numbers >= 80:
#     print("Your Grade is B");
# elif std_numbers < 80 and std_numbers >= 70:
#     print("Your Grade is C");
# elif std_numbers < 70 and std_numbers >= 60:
#     print("Your Grade is D");
# elif std_numbers < 60 and std_numbers >= 0:
#     print("You'r Failed");
# else:
#     print("The number must be in the range of 0 to 100")


std_numbers = int(input("Enter Your Numbers: "));

if  90 <= std_numbers <= 100:     
    print("Your Grade is A");
elif std_numbers < 90 and std_numbers >= 80:
    print("Your Grade is B");
elif std_numbers < 80 and std_numbers >= 70:
    print("Your Grade is C");
elif std_numbers < 70 and std_numbers >= 60:
    print("Your Grade is D");
elif std_numbers < 60 and std_numbers >= 0:
    print("You'r Failed");
else:
    print("The number must be in the range of 0 to 100")