z=int(input("enter the year: "))
if z<1582:
    print("Not within Gregorian Calendar")
elif z%4 !=0:
    print("common year")
elif z%100 !=0:
    print("leap year")
elif z%400 !=0:
    print("common year")
else:
    print("leap year")
