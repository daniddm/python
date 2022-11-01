import re
import xml
import os

path = 'C:/Users/danie/Documents/PROGRAMAR/python/python-100_days/python/xml'
pattern = (r'(\d+)')
 

 
fun = lambda x : os.path.isfile(os.path.join(path,x))
 
files_list = filter(fun, os.listdir(path))
print(files_list)
# Create a list of files
# in directory along with the size
size_of_file = [
    (f,os.stat(os.path.join(path, f)).st_size)
    for f in files_list
]

 
# in this case we have use its file name.
for f,s in sorted(size_of_file):
    

    print(f,pattern)