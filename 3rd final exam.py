input_number=int(input("please enter a number: "))
p=0
q=1
if (input_number%1==0 and input_number>0):
    while (input_number//q>0):
        p=p+1
        q=q*10
    print(p)
else:print("input is not valid")


