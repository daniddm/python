
# ELSE IF 
# par e impar 
# number = int(input("choose a number :"))

# if number % 2 == 0:
#     print("the number is odd")
# else:
#     print("the number in even")

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

if weight < 18.5:
    print("they are under weight")
elif weight > 18.5 and weight < 25:
    print("they are normal")
elif weight> 25 and weight <30:
    print("are slightly overweight")
elif weight > 30 and weight <35:
    print("are  super")
else:
    print("are  overweight")