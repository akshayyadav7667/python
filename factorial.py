
num= int(input("Enter the number to find the factorial :- "))

def factorial(num):
    if(num==0 or num==1):
        return 1
    return num * factorial(num-1)

fact=factorial(num)
print(fact)