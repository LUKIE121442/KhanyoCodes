#Getting user input
while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

#Step 1: What we did what getting user input but since that user inpt are string
#        we then use num=float(num1 so that we can convert it into numbers

#Adding operation ( + - * /)
    operation= input("Enter operation (+,-, *, /): ")

#Adding logic to our code (IF STATEMENTS)

    if operation == "+":
        print(num1 + num2)
 
    elif operation == "-":
        print(num1 - num2)
 
    elif operation == "*":
        print(num1 * num2)

#{
# elif operation == " / ":
# print(num1 / num2)
# } for devision we could use the code above but we want to prevent crashing when a user tries dividing by 0

    elif operation == "/":
        if num2 == 0 :
            print("Cannot divide by zero!")
        else:
            print(num1 / num2)

#If a user doesnt use any giving operation then it should print invalid.
    else:
        print("INVALID OPERATOR")
       
    again = input("Do you want to continue? (yes/no): ")
    if again == "no":
        break

 





