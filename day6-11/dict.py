programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
                          "Function": "A piece of code that you can easily call over and over again."}


print(programming_dictionary["Bug"])
programming_dictionary["loop"] = "the loop is the action doing something over and over again."



# crear un diccionario
empyt_dictionary = {}

# edit a bug

programming_dictionary["loop"] = "changes in the loop now"
print(programming_dictionary)


#loop through a dictionary

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])