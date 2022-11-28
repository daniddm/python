import pandas as pd

student_dict = {
 "student": ["Angela","Daniel", "Blanca","MErche"],
 "score":[23,45,55,88]   
}

#looping throw dictionary

for (key,value) in student_dict.items():
    print(value)

student_data_frame = pd.DataFrame(student_dict)

# print(student_data_frame)

#loop through rows os data frame

for (index, row) in student_data_frame.iterrows():
    # print(row) obtain one object in the dataframe
    print(row.score)