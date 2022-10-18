bill = float(input("what's the total bill ? "))
tip = int(input("how much tip would you givr? 10,12 or 15 ? "))
people = int(input("people to split ? "))

tip_per = tip/100
total = bill * tip_per
total_tip = bill + total
bill_p_person = total_tip/people

final_amount= "{:.2f}".format(bill_p_person)

print(f"each person should pay: ${final_amount}")