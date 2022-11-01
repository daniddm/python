
h = int(input("the height of the wall ? "))
w = int(input("the weight of the wall ? "))

def paint_calc( a, b , c):
    numbers_cans = (a * b) / c
    number_rounded = round(numbers_cans)
    print(number_rounded)

c= 5
paint_calc(h,w,c)