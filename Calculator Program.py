print ("Hello, Welcome to my first calculator program!")
print ("to use this program, we need to have your name and age to continue")
name = input("Enter your name please : ")
age = input ("enter your age please : ")
email = input ("Enter your email please :")
print ("Hello " + name + " you are " + age + "years old")
print (" Welcome " + name + " to my first calculator program! Hope you are enjoying this program!")

while True:
    print ("This program is a simple calculator that can perform basic arithmetic operations.")
    print ("You can add, subtract, multiply, or divide two numbers.")
    print ("Let's get started!")
    print ("Please enter your first number:")
    first_number = int(input())
    print ("Please enter your second number:")
    second_number = int(input())
    print ("Great! Now we can do some calculations with your numbers.")
    print ("Please choose an operation:")
    print ("1. Addition")
    print ("2. Subtraction")
    print ("3. Multiplication")
    print ("4. Division")
    operation = input("Enter the number of the operation you want to perform: ")
    if operation == "1":
        result = first_number + second_number
        print("The result of the addition is: " + str(result))
    elif operation == "2":
        result = first_number - second_number
        print("The result of the subtraction is: " + str(result))
    elif operation == "3":
        result = first_number * second_number
        print("The result of the multiplication is: " + str(result))
    elif operation == "4":
        if second_number != 0:
            result = first_number / second_number
            print("The result of the division is: " + str(result))
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("I'm sorry, but the operation you entered is not valid. Please try again. Good Luck!")

    again = input("Do you want to use the calculator again? (yes/no): ")
    if again.lower() != "yes":
        print("Thank you for using my calculator program, " + name + "! Have a great day!")
        break
