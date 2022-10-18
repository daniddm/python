
bill = float (input('what is the bill ? '))
people = int (input ("how many people to split the bill ? "))
porcentage = int (input ("what´s the tip would you like to give ? "))

tip_total = porcentage / 100
total_bill = (bill * tip_total) + bill
result = total_bill/people

print(f"total for pay: ${result}")