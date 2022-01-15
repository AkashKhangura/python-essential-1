secret_number=777
n=int(input("Enter the number: "))
while n!=secret_number:
    if n<secret_number:
        print("ha ha ! you are stuck in my loop! the secret number is larger than your guessed number")
    elif n>secret_number:
           print("ha ha ! you are stuck in my loop! the secret number is smaller than your guessed number")
    n=int(input("try again"))
print("well done, muggle! you are free now")
