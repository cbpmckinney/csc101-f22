
#Conditional Expressions
#Need a Boolean expression (something that evaluates to true/false)
numstudents = 35

if(numstudents > 1):
    print("Several dudes are hungry!")
elif(numstudents == 1): #elif is short for else if
    print("Exactly one dude is hungry!")
else:
    print("Nobody is hungry!")

# 2 <= numstudents <= 10
if((numstudents >= 2) or (numstudents <= 10)):
    print("Nice.")