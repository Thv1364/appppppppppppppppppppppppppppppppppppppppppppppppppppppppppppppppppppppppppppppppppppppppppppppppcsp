#!!!!!!!DELETE LATER!!!!!!!!!
#!!!!!!!DELETE LATER!!!!!!!!!
#!!!!!!!DELETE LATER!!!!!!!!!
#!!!!!!!DELETE LATER!!!!!!!!!
#!!!!!!!DELETE LATER!!!!!!!!!

#Complete? Need:

#Nope      Input with instructions
#Nope      List
#Nope      Function
#Nope      Parameter to function
#Nope      Loops
#Nope      If
#Nope      Variable changing with lists
#Nope      Call function

assignments={
    "a":[0,10]
    }

total_amount = int(input("How many total assigments (including tests) would you like to \"grade\"? \n"))
current_graded=0



def add_assignment(assignment, done, outof):
    if done=="yes":
        done=1
    else:
        done=0
    assignments[assignment]=[done,outof]



# def averageit():
#     nume=0
#     denom=0
#     for assignment in assignments:
#         print("it is" + assignment)
#         nume=intassignment[0]+int(nume)
#         denom=assignment[1]+denom
#     avg=nume/denom
#     print(str(avg))

averageit()

while current_graded<total_amount:
    add_assignment(input("What is the assignment named?"),input("Was the assignment submitted? Type yes or no."),int(input("Out of how many points?")))
    current_graded=current_graded+1


