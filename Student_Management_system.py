from src.services import ( # import the functions within the file in the src path
    menu, # menu function
    add_student, # function to add students
    see_list, # function to view the list of students
    search_student, # function to search for student
    update_student, # function to update student
    delete_student, # function to delete student
)

students = [] # empty list where students will be stored


op = 0 # variable created for the options

while op < 6: # while loop to start a loop while the variable op is less than 6
    menu() # we call the menu
    try: # Error handling begins
        option = int(input("Choose an option: ")) # variable to store the option
        if option <= 0 or option > 6: # If condition to check that the entered number is not less than zero and greater than 6
            print("Please enter a menu option(1-6)") # displays a message to the user
            continue # It asks you to choose an option again.
    except ValueError: # in case it is a text string
        print("Please enter only numeric values") # show this message
        continue # It asks you to choose an option again.

    if option == 1: # condition in case the option is 1
        Id = 0 # variable for the while
        while Id == 0: # condition for the loop to run
            try: # # Error handling begins
                Id = int(input("Enter your ID: ")) # Ask the user for the ID
                if Id <= 0: # condition to verify that the id is positive
                    Id = 0 # The ID is set to 0 to continue the cycle
                    print("Please enter positive numbers") # shows a message
                    continue # Ask for the ID again
            except ValueError: # in case it is a text string
                print("Please enter only numeric values") # shows a message
                continue # Ask for the ID again
        name = 0 # variable for the while
        while name == 0: # condition for the loop to run
            try: # Error handling begins
                name = input("Enter your name: ") # ask for the name
                if name == "": # condition in case it is a blank space
                    name = 0 # The name is set to 0 to continue the cycle
                    print("Please enter a name") # shows a message
                    continue # Ask for the name again
            except Exception: # in case it is a number
                continue # Ask for the name again
        age = 0 # variable for the while
        while age == 0: # condition for the loop to run
            try: # Error handling begins
                age = int(input("Enter your age: ")) # ask the age
                if age <= 0: # condition to verify that the age is positive
                    age = 0 # The age is set to 0 to continue the cycle
                    print("Age must be greater than zero") # shows a message
                    continue # Ask for the age again
                elif age >= 100: # condition to verify that the age is less than 100
                    age = 0 # The age is set to 0 to continue the cycle
                    print("Limit Age -> 99") # shows a message
                    continue # Ask for the age again
            except ValueError: # in case it is a text string
                print("Please enter only numeric values") # shows this message
        program = input("Enter your program: ") # request the program or course
        status = input("Enter your current status: ") # asks for current status
        add_student(students, Id, name, age, program, status) # Call the add_student function and pass it the arguments

    elif option == 2: # # condition in case the option is 2
        if len(students) == 0: # check if the list is empty
            print("The list is empty") # Show this message
        else: # in case no
            see_list(students) # It calls the see_list function and passes the list as an argument

    elif option == 3: # condition in case the option is 3
        if len(students) == 0: # check if the list is empty
            print("The list is empty") # Show this message
        else: # in case no
            id_search = 0 # variable for the while
            while id_search == 0: # condition for the loop to run
                try: # Error handling begins
                    id_search = int(input("Enter your ID: ")) # request the ID to search
                    if id_search <= 0: # condition to verify that the id is positive
                        id_search = 0 # The id_search is set to 0 to continue the cycle
                        print("Please enter positive numbers") # Shows a message
                        continue # Ask for the id again
                except ValueError: # in case it is a text string
                    print("Please enter only numeric values") # Show this message
                search_student(students, id_search) # It calls the search_student function and passes it the arguments

    elif option == 4: # condition in case the option is 4
        if len(students) == 0: # check if the list is empty
            print("The list is empty") # # show this message
        else:
            id_search = 0 # variable for the while
            while id_search == 0: # condition for the loop to run
                try: # Error handling begins
                    id_search = int(input("Enter your ID: ")) # request the ID to search
                    if id_search <= 0: # condition to verify that the id is positive
                        id_search = 0 # The id_search is set to 0 to continue the cycle
                        print("Please enter positive numbers") # Shows a message
                        continue # Ask for the id again
                except ValueError: # in case it is a text string
                    print("Please enter only numeric values") # Show this message
            for us in students: # for loop to iterate through the list
                if us["ID"] == id_search: # condition to check if id within the list is equal to id to search
                    print("Student found. Enter new information\n") # Show this message
                    new_name = input("Enter your new name: ") # ask for the new name
                    new_age = 0 # variable for the while
                    while new_age == 0: # condition for the loop to run
                        try: # Error handling begins
                            new_age = int(input("Enter your new age: ")) # ask for the new age
                            if new_age <= 0: # condition to verify that the age is positive
                                new_age = 0 # The new_age is set to 0 to continue the cycle
                                print("Age must be greater than zero") # Show this message
                                continue # Ask for the age again
                            elif new_age >= 100: # condition to verify that the age is less than 100
                                new_age = 0 # The new_age is set to 0 to continue the cycle
                                print("Limit age -> 99") # Show this message
                                continue # Ask for the age again
                        except ValueError: # in case it is a text string
                            print("Please enter only numeric values") # Show this message

                    new_program = input("Enter your new program: ") # ask for the new program or course
                    new_status = input("Enter your new current status: ") # ask for the new current status
                    update_student(students, new_name, new_age, new_program, new_status) # It calls the update_student function and passes it the arguments

                else: # in case the student does not exist
                    print("Student not found!") # Show this message

    elif option == 5: # condition in case the option is 5
        if len(students) == 0: # check if the list is empty
            print("The list is empty") # Show this message
        else: # in case it is not empty
            id_delete = 0 # variable for the while
            while id_delete == 0: # condition for the loop to run
                try: # Error handling begins
                    id_delete = int(input("Enter the ID to delete: ")) # Request the ID to delete
                    if id_delete <= 0: # condition to verify that the id is positive
                        id_delete = 0 # The id_delete is set to 0 to continue the cycle
                        print("Please enter positive numbers") # Show this message
                        continue # Ask for the id again
                except ValueError: # in case it is a text string
                    print("Please enter only numeric values") # Show this message
            delete_student(students, id_delete) # It calls the delete_student function and passes it the arguments

    elif option == 6: # condition in case the option is 6
        leave = input("Are you sure you want to exit? S/N: ").upper() # asks the user if they want to exit and converts everything to uppercase
        if leave == "S": # in case it is 's'
            print("Leaving...") # # Show this message
            break # Everything breaks and the program closes
        elif leave == "N": # in case it is 'n'
            continue # Go back to the start and show the menu