# -----Author -> Huzaifa Ameer---------------#
# -----Variable initialization-------
total = 0
st_count = 0
ast = "*"
option = "y"
outcome=""

# ------Histogram Variables
progressCount = 0
trailerCount = 0
retrieverCount = 0
excludedCount = 0

# ------Credits List--------
student_details = []

# -----------function to check the validity---------------
def check_Student_credits(message):
    #checks the validity of the input credits
    str_error = "\tInteger Required."
    range_error = "\tOut of Range"
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
# --------------------------------------------------------
# -----------function to print the histogram--------------
def histogram(pC, tC, rC, eC, sC):
    print("\n")
    print("---------------------------------------------")
    print("Histogram")
    print(f"Progress {pC}  : {ast * pC}")
    print(f"Trailer {tC}   : {ast * tC}")
    print(f"Exclude {eC}   : {ast * eC}")
    print(f"Retriever {rC} : {ast * rC}")

    print(sC, " outcomes in the total.")
    print("---------------------------------------------")
# --------------------------------------------------------


while (option == "y"):
    #getting the credits through the check_Student_credits function
    pass_credit = check_Student_credits("Please enter your credits at pass : ")
    defer_credit = check_Student_credits("Please enter your credits at defer : ")
    fail_credit = check_Student_credits("Please enter your credits at fail : ")
    
    #adding the credits to credit_details
    credit_details=[pass_credit,defer_credit,fail_credit]
    
    #calculate the total
    total = pass_credit + defer_credit + fail_credit

    if (total != 120):
        print("\tTotal incorrect.")
    else:
        st_count += 1
        #checking the credits and assigning the progression outcome
        if (pass_credit == 120):
            outcome="progress"
            progressCount += 1
        elif (pass_credit == 100):
            outcome="progress (module trailer)"
            trailerCount += 1
        elif (fail_credit == 80 or fail_credit == 100 or fail_credit == 120):
            outcome="Exclude"
            excludedCount += 1
        else:
            outcome="Do not progress – module retriever "
            retrieverCount += 1
        print(outcome)
        
        #appending the outcome to credit_details
        credit_details.append(outcome)

        #appending the inner list to the outer list
        student_details.append(credit_details)

    print("\n")
    while True:
        print("Would you like to enter another set of data? ")
        option = input("Enter 'y' for yes or 'q' to quit and view results:")
        #get new information or quit, and print the obtained outcomes

        if (option == "q"):
            histogram(progressCount, trailerCount, retrieverCount, excludedCount, st_count)
            print("Part 02")
            #creates the text file
            file1=open("StudentCredits.txt","w")
            file1.write("Part 03")
            file1.write("\n")
            for i in student_details:
                x = str(i[0:3])#casting the 3 credits into string
                
                x = x.replace("[", "")#replaces the '['with a space 
                x = x.replace("]", "")#replaces the ']'with a space
                print(i[-1],"-",x)#prints the obtained details 

                #statements for text file data writing
                file1.write(i[-1])
                file1.write(" - ")
                file1.write(x)
                file1.write("\n")
            #closes the opened file
            file1.close()
            break
        elif (option == "y"):
            break
        else:
            print("\tPlease enter the correct option !")    
        continue
    print("\n")

# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1956114 / 20221354 
# Date: 12/12/2022
