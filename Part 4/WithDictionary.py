# -----Huzaifa Ameer---------------#
# -----Variable initialization-------
total = 0
option = "y"
outcome = ""
# ------Student Details Dictionary--------
student_details = {}
# -----------function for check the validity-------------
def check_Student_credits(message):
    str_error = "\tInteger Required."
    range_error = "\tOut of Range"
    #checks the validity of the input credits
    while True:
        try:
            marks = int(input(message))
        except ValueError:
            print(str_error)
            continue
        if marks not in range(0, 121, 20):
            print(range_error)
            continue
        break
    return marks

# -------------------------------------------------------
while (option == "y"):
    #asking for the student id 
    student_id=input("Please enter the your ID number : ")
    if student_id in student_details:
        print("The student id is already exists. Please try again !")
        continue
    #get the valid values for the credit variables
    pass_credit = check_Student_credits("Please enter your credits at pass : ")
    defer_credit = check_Student_credits("Please enter your credits at defer : ")
    fail_credit = check_Student_credits("Please enter your credits at fail : ")

    credit_types = [pass_credit, defer_credit, fail_credit] #adding the credits into the list
    total = pass_credit + defer_credit + fail_credit #calculating the total

    #checks the total and adds the id and the list to the dictionary
    if (total != 120):
        print("\tTotal incorrect.")
    else:
        if (pass_credit == 120):
            outcome = "progress"
        elif (pass_credit == 100):
            outcome = "progress (module trailer)"
        elif (fail_credit == 80 or fail_credit == 100 or fail_credit == 120):
            outcome = "Exclude"
        else:
            outcome = "Do not progress – module retriever "
            print("\n")
        print(outcome)
        credit_types.append(outcome)
        student_details[student_id]=credit_types #assingning the values for the dictionary
    print("\n")
    while True:
        print("Would you like to enter another set of data? ")
        option = input("Enter 'y' for yes or 'q' to quit and view results:")

        if (option == "q"):
            print("\n")
            #prints the details through the dictionary
            for key,value in student_details.items():
                x = str(value[0:3])#casting int into string
                x = x.replace("[", "")
                x = x.replace("]", "")
                print(key,":",value[-1],"-",x)
            break
        elif (option == "y"):
            break
        else:
            print("\tPlease enter the correct option !")#prints when the input option is incorrect    
        continue
    print("\n")
    
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1956114 / 20221354 
# Date: 12/12/2022

