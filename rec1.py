def Exercise(n):
    print(2*n)
    if (n < 3):
        Exercise(n+1)
    print(3*n)