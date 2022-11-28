numbers = [1,2,3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

print(new_list)


#list comprehension
# new_list = [new_item for item in list]
# list = en que lista se va a iterar
# item en la lista , lo podemos llamar como queramos
# new_item es la expresion 

list = [n + 1 for n in numbers]
print(list)

name = "Daniel"
n_list = [letter for letter in name]
print(n_list)

range(1,5)

double_num = [n*2  for n in range(1,5)]
print(double_num)

names = ["Daniel", "Mercedes", "Blanca","Marta"]

short_names1 = [name for name in names if len(name) < 6] # sale Marta solo por la longitud del nombre


short_names1 = [name.upper() for name in names if len(name) < 6] # sale MARTA solo por la longitud del nombre
print(short_names1)
