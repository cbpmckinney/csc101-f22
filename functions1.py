from math import sqrt

#f(n) = n*n
def square(n):
    ans = n*n
    return ans

def squareroot(n):
    if(n<0):
        print("You can't take the sqrt of a negative!")
        return "You dummy!"
    else:
        ans = sqrt(n)
        return ans

def power(number,pow):
    ans = 1
    if(pow == 0):
        return 1
    elif(pow == 1):
        return number
    else:
        ans = number*power(number,pow-1) 
        return ans




print(power(2,4))
