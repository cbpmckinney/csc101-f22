from math import sqrt

#f(x) = x^2 or f(x) = x*x
def square(x):
    ans = x*x
    return ans

def multiply(x,y):
    ans = x*y
    return ans

def squareroot(x):
    if(x>=0):
        return sqrt(x)
    else:
        print("You moron!")

def absval(x):
    if(x>=0):
        return x
    else:
        return -x

def power(number,pow):
    ans = 1
    if(pow == 0):
        return 1
    elif(pow == 1):
        return number
    else:
        for i in range(0,pow):
           ans = number*ans 
        return ans


def factorial(num):
    ans = 1
    if(num == 0):
        return ans
    if(num == 1):
        return ans
    else:
        for i in range(num,1,-1): #range(1num+1) = [1,num+1)
            ans = ans*i
        return ans

def recfactorial(num):
    if(num==0):
        return 1
    else:
        return   num*recfactorial(num-1)

print(factorial(5))

#5! = 5*4*3*2*1
#5! = 5*(4*3*2*1) = 5*4!
#n! = n*(n-1)!, 0!=1