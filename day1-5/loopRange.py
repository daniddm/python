
number = 0

x = range(1,100)
for i in x:
    number = i
    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 5 == 0 and number % 2 == 0:
        print("FizzBuzz")
    else:
        print(number)
