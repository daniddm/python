

arr= [2, 2, 2, 2, 2, 2]

def grow(arr):
    result = 1
    for i in arr:
        result = result*i
    return result

print(grow(arr))