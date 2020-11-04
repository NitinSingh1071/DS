def factorial(num):
    fact = 1
    while (num>0):
        fact = fact * num
        num = num - 1
    return fact

def factorial_recursion(num):
    if num == 1:
        return num
    else :
        return num*factorial_recursion(num-1)


def factors_num(num):
    for i in range(1,num+1):
        if (num%i)==0:
            print(i, end =" ")

def factors_recursion(num,x):
    if x <= num:
        if (num % x == 0):
            print(x, end =" ")
        factors_recursion(num, x + 1)
        

num = 11
print(f"Factorial of {num} is {factorial(num)}")
print(f"Factorial of {num} using recursion is {factorial_recursion(num)}")
print(f"Factors of {num} : ")
factors_num(num)
print(f"\nFactors of {num} using recursion :")
print(factors_recursion(num,1))
