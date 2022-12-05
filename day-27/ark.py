# class Car:
    
#     def __init__(self, **kw) -> None:
#         self.make = kw.get("make")
#         self.model = kw.get("model")

# my_car = Car (make ="Nissan", model = "GT")

# print(my_car.model) 


def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)
 
bar(1, 2)
