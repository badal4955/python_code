# if statement

# age=int(input("enter age :"))
# if age>18:
#     print("you are adult")
#     print("hangout")

# if else statement

# age=int(input("enter age :"))
# if age>18:
#     print("you are adult")
# else:
#     print("you are not adult!")

#elif statement

# age=int(input("enter age :"))

# if age>15 and age<19:
#     print("you are teenager")
# elif age>19:
#     print("you are adult!")
# else:
#     print("you are children!")

# nested if statement

# Get the user's age as an integer
age = int(input("Enter age: "))

# Get the user's input on car ownership
own_car = input("Do you own a car? (True/False): ")

# Convert the input to a boolean value
own_car = own_car.lower() == 'true'

# Check if the user is old enough to drive
if age >= 18:
    if own_car:
        print("Drive your car")
    else:
        print("Rent a car!")
else:
    print("You can't drive underage!")