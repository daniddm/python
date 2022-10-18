# fruits = ["apple","peach","pear"]


# for f in fruits:
#     print(f)

# fruit_len = len(fruits)
# print(fruit_len)


student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


print(student_heights)

height = 0
for h in student_heights:
    print(h)
    height += h
   

print(height)

total_student = 0
for s in student_heights:
    total_student += 1
print(total_student)


max_number = student_heights[0]

for n in student_heights:
  
  if n > max_number:
      max_number  = n 
      print(max_number)