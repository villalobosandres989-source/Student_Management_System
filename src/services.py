def menu(): # Create a function called menu
    print("\n=== MAIN MENU ===") # show this message
    print("1. Add Student") # show this message
    print("2. See the list of students") # show this message
    print("3. Search student") # show this message
    print("4. Update student information") # show this message
    print("5. Delete student") # show this message
    print("6. Exit") # show this message


def add_student(students, ID, name, age, program, status): # Create a function called add_student and receive those parameters
    list = {"ID": ID, "Name": name, "Age": age, "Program": program, "Status": status} # Create a dictionary with these keys and values

    students.append(list) # Add the dictionary to the student list
    print("Student successfully added!") # show this message


def see_list(students): # Create a function called see_list and receive this parameters
    for u, student in enumerate(students, start=1): # Use a for loop to iterate through the list and count the indices with the enumerate function. By default it starts at 0, but with start=1 it starts at 1
        print(
            f"{u}. ID: {student['ID']} || Name: {student['Name']} || Age: {student['Age']} || Program: {student['Program']} || Status: {student['Status']}"
        ) # displays the list of students


def search_student(students, ID): # Create a function called search_student and receive those parameters
    for people in students: # use a for loop to iterate through the list
        if ID == people["ID"]: # condition to check if the list id is equal to the id to search for
            print("Student Found!!") # show this message

            print(
                f"ID: {people['ID']} || Name: {people['Name']} || Age: {people['Age']} || Program: {people['Program']} || Status: {people['Status']}"
            ) # shows the student wanted
            break
    else: # in case it does not exist
        print("Student not found!") # show this message


def update_student(students, new_name, new_age, new_program, new_status): # Create a function called update_student and receive those parameters
    for x in students: # use a for loop to iterate through the list
        x["Name"] = new_name # assign a new value to the dictionary key within the list
        x["Age"] = new_age # assign a new value to the dictionary key within the list
        x["Program"] = new_program # assign a new value to the dictionary key within the list
        x["Status"] = new_status # assign a new value to the dictionary key within the list

        print("Student updated successfully!") # show this message


def delete_student(students, ID): # Create a function called delete_student and receive those parameters
    for y in students: # use a for loop to iterate through the list
        if y["ID"] == ID: # condition to check if the list id is equal to the id to search for

            students.remove(y) # removes the user from the list
            print("Student successfully removed") # show this message
            break # breaks the for loop
    else: # in case it does not exist
        print("Student not found!") # show this message
