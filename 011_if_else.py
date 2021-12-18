x=float(input("hey enter the income: "))
if x<85528 :
    y=(0.18*x)-556.02
    if y<=0 :
        print("if no money return")
    else:
            print("what is the tax: ",y)
else:
    print("what is the tax: ",14839.02+((x-85525)*0.32))
