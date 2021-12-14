HH=int(input("Give me the start time(hour): "))
MM=int(input("Give me the start time(Minute): "))
DD=int(input("Give me the duration in minutes: "))
RR=(HH*60)+MM+DD
print("The finish time is: ",end="")
print(RR//60,RR%60,sep=":")
