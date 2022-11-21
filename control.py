
#Declarative/Imperative Expressions

print("Hello, world!")
x = 5
y = 7
print(x+y)

#Conditionals
#Must have a boolean expression: something that evaluates to true or false
if(x > 3):
    print("x is greater than 3!")
elif(x == 2): #elif is short for else if
    print("x equals 2")
else:
    print("x is not greater than 3!")

if((x > 3) and (y < 7)):
    print("waffles")

print("I like sandwiches!")

#Iterative expressions: three kinds
#while, do-while, for
#for is a special case of while
while(x > 0):
    print(x)
    x = x-1


x=5
while True:
    print(x)
    x = x-1
    if(x <= 0):
        break

for i in range(0,y):
    print(i)
