# try: 
#     a = 10
#     b = 2
#     print('Execution started')
#     print(a + b)
#     print(a - b)
#     print(a * b)
#     print(a / b)
# except ZeroDivisionError :
#     print("Error:Division by zero is not allowed")
# print("Execution completd")




# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     print("Result:", a / b)
# except ZeroDivisionError:
#     print("Error:Division by zero is not allowed")
# except ValueError:
#     print("Invalid input. Please enter valid integer")
# print("Execution completed")


# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     print("Result:", a / b)
# except (ZeroDivisionError,ValueError) as e:
#     print(e)


# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     print("Result:", a / b)
# except (ZeroDivisionError,ValueError) as e:
#     print(e)
# else:
#     print("No exception occured")
# print("Execution completed")

try:
    print("Execution started")
    a = int(input("Enter a number: "))
    print("The value of a is :",a)
except ZeroDivisionError as e:
    print(e)
finally:
    print("I am finally")
print("Execution completed")