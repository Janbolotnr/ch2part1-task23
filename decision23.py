y = int(input("Year: "))
if y % 4 != 0:
    print("usual year")
elif y % 100 == 0:
    if y % 400 == 0:
        print("intercalary year")
    else:
        print("usual year")
else:
    print("intercalary year")            

