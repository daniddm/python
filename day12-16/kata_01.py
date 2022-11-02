# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.

# Example
arr = []



    
def longitud(mi_lista):
    cont = 0
    negative = 0
    
    
    for i in mi_lista :
        if i > 0:
            cont += 1
        elif i < 0: 
            negative = negative + i
        elif not arr:
            return []
    return [cont , negative]



print(longitud(arr))

