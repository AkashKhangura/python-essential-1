n=int(input("enter any natural number: "))
print("the divisors of the number are: ")
for i in range (1,n//2+1):
    if (n%i)==0:
        print(i,end=", ")
print(n)
print("the end.")
