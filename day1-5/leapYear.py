year = int(input("choose one year ? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("year is leap")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
    print("the year is not leap")