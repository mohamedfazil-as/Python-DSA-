#  Recursion -->  calling a function  repeatedly
# A function is a block of reusable code that performs a specific task.

#  Factorial :

n =  5

def fact(n):
    if n==1:  #Base conditon
        return 1
    return n*fact(n-1)
print(fact(n))






