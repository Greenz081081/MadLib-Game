# # Topic: Functions

# from datetime import datetime
# # This is a sample of completing this task without a function
# first_name = "susan"
# print("Task Completed")
# print(datetime.now())
# print()

# for y in range(0,11):
#     print(y)
# print("The for loop completed")
# print(datetime.now())
# print()




# #This is a sample of completing the task with a function
# # Function: To print current time and date
# def print_time():
#     print("The task is completed") 
#     print(datetime.now())  
#     print()

# first_name = "Susan"
# print_time()


# for x in range(0,11):
#     print(x)
# print()
# print_time()




# # Sample of the code i can use if i want to display different text 
# def print_time(name):
#     print(name) 
#     print(datetime.now())  
#     print()

# first_name = "Susan"
# print_time("Printed fthe first name")


# for x in range(0,11):
#     print(x)
# print()
# print_time("Completed for loop")




# # Getting Initials without using a function
# first_name = input("Please Enter Your First Name:") 
# first_name_initials = first_name[0:1]

# middle_name = input("Please Enter Your Middle Name:")
# middle_name_initials = middle_name[0:1]

# last_name = input("Please Enter Your Last Name:")
# last_name_initials = last_name[0:1]
# print()

# print(f"Your Initials Are: {first_name_initials}{middle_name_initials}{last_name_initials}")
# print("Your Initials Are: " + first_name_initials \
#     + middle_name_initials + last_name_initials)





# # Getting Initials using a function
# # This function will return the initials of a name
# def get_initial(name):
#     initial = name[0:1]
#     return initial.upper()
# # Ask for someone's name and return the initials
# first_name = input("Please Enter Your First Name:") 
# first_name_initials = get_initial(first_name)

# middle_name = input("Please Enter Your Middle Name:")
# middle_name_initials = get_initial(middle_name)

# last_name = input("Please Enter Your Last Name:")
# last_name_initials = get_initial(last_name)
# print()

# print(f"Your Initials Are: {first_name_initials}{middle_name_initials}{last_name_initials}")


# You can specify a default value for a parameter
# def get_initial(name, force_uppercase = True):
#     if force_uppercase:
#         initial = name[0:1].upper()

#     else:
#         initial = name[0:1]
#     return initial

# first_name = input("Please Enter Your first Name:")
# first_name_initials = get_initial(first_name)

# middle_name = input("Please Enter Your Middle name:")
# middle_name_initials = get_initial(middle_name)

# last_name = input("Please Enter Your Last Name:")
# last_name_initials = get_initial(last_name)

# print(f"Your Initial is: {first_name_initials}{middle_name_initials}{last_name_initials}") 


# Using the named notation when calling function makes your code readable
def error_logger(error_code, error_severity, log_to_db, \
    error_message, source_module):
    print(f"Oh no! " + error_message)
# Imagine code here that logs out error to a database or file
first_number = 10
second_number = 5
if first_number < second_number:
    error_logger(error_code = 45, error_severity = 1,
     log_to_db = True,
     error_message = "Second number greater than first",
     source_module = "My_math_module")



