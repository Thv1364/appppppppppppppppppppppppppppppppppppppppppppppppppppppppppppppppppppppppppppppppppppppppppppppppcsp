import random
import time
import webbrowser

assignments={

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
    time.sleep(2)
    print("Thank you for using this service. You will recieve a quick form. Please fill it out and provide recommendations.")
    time.sleep(4)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("0")
    time.sleep(1)





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

def graders(assig):
    counter=0
    for assignment in assig:

        if counter < random.randint(4,7):
            assign=assig[assignment]
            temp=grader(assign, 1)
            assig[assignment]=temp
            counter=counter+1
        else:
            assign=assig[assignment]
            temp=grader(assign, 0)
            assig[assignment]=temp
            counter=0
    print(assig)
    return assig
        

def veryusefulthing():
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=0)


setup()
assignments=graders(assignments)
averageit()
veryusefulthing()