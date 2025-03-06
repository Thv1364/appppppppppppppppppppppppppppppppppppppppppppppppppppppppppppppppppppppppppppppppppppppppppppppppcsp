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


import random


assignments={
"a": [1,11],   
"b": [1,21],   
"c": [1,31], 
"d": [1,11],  
"e": [1,21], 
"f": [1,31],   
"g": [1,11],   
"h": [1,21],   
"i": [1,31],   
"j": [1,11],
"k": [1,11],      
"l": [1,11],      
"m": [1,11],      
"n": [1,11],            
    }

total_amount = int(input("How many total assigments (including tests) would you like to \"grade\"? \n"))




def add_assignment(assignment, done, outof):
    assignments[assignment]=[done,outof]



def averageit():
    numer=0
    denom=0
    for assignment in assignments:
        assign=assignments[assignment]
        numer=numer+assign[0]
        denom=denom+assign[1]
    print("You have " +str(numer) + " points out of " + str(denom) + " points. \n")
    avg=numer*100/denom
    print("Therefore, you have a " + str(avg) + "%. Great Job!")




def setup():
    current_graded=0
    while current_graded<total_amount:
        print("\n")
        add_assignment(input("What is the assignment named? You have added " + str(current_graded) + " assignment(s) so far. \n"),input("Was the assignment submitted? Type 1 for yes or 0 for no. \n"),int(input("How many points was the assignment worth? \n")))
        current_graded=current_graded+1

def grader(h,question):
    if question==1:
        h[0]=int(h[0])*int(h[1])
    else:
        h[0]=int(h[0])*int(h[1])*0.9
    return(h)

def graders():
    counter=0
    for assignment in assignments:
        
        if counter < random.randint(4,7):
            assign=assignments[assignment]
            temp=grader(assign, 1)
            assignments[assignment]=temp
            counter=counter+1
        else:
            assign=assignments[assignment]
            temp=grader(assign, 0)
            assignments[assignment]=temp
            counter=0
    print(assignments)

    
        


        


# def veryusefulthing():






# setup()
graders()
averageit()
# veryusefulthing()
# returner()

