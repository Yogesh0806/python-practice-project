#  Dataset: Create a CSV with 25 students: name, age, city, marks in 5 subjects.

import csv

records = [
['Name','Age','City','Maths','Science','English','Computer','History','Study_Hours'],
['Aman',20,'Bhopal',78,82,75,88,80,4],
['Riya',19,'Indore',90,91,89,95,88,6],
['Mohit',21,'Gwalior',65,70,68,72,66,3],
['Priya',20,'Bhopal',85,88,92,85,87,5],
['Rahul',22,'Indore',55,60,58,62,59,2],
['Sneha   ',20,'Jabalpur',92,95,94,97,96,7],
['Karan',21,'Gwalior',70,72,68,94,75,71,],
['Neha',19,'Indore',88,90,86,91,89,6],
['Vikas',22,'Bhopal',45,50,48,52,49,1],
['Pooja',20,'Jabalpur',80,84,82,86,81,5],
['Rohit',21,'Indore',76,78,74,80,77,4],
['Anjali',19,'Gwalior',95,94,96,98,97,8],
['Deepak',20,'Bhopal',67,69,71,73,70,3],
['  Nisha',21,'Jabalpur',83,85,88,74,84,5],
['Arjun',20,'Indore',72,75,73,78,74,4],
['Komal',22,'Bhopal',89,87,90,91,88,6],
['Yash',21,'Gwalior',60,62,61,65,63,2],
['Tina',20,'Jabalpur',91,92,93,94,95,7],
['Harsh',19,'Indore',77,79,80,81,78,4],
['Meena',21,'Bhopal',68,70,69,72 ,71,3],
['Sagar',20,'Gwalior',52,55,54,58,56,2],
['delDivya',22,'Jabalpur',86,88,89,90,87,6],
['Ajay',21,'Indore',74,76,78,79,75,4],
['Kriti',20,'Bhopal',93,94,92,95,91,7],
['Manish',22,'Gwalior',75,60,62,64,61,2],
 ]

# with open('student.csv','w',newline='') as f:
#     csv.writer(f).writerows(records)
    
'''Tasks:
  1. Load CSV with Pandas. Handle missing values and errors.'''


import pandas as pd 
df = pd.read_csv('student.csv')
# # print(df.head())    

# print(df.isnull().sum())

df['Name'] = df['Name'].str.strip()
# print(df['Name'])

#For Errors handling
# try:
#     df = pd.read_csv("students.csv")
#     print("File loaded successfully")
# except FileNotFoundError:
#     print("Error: students.csv file not found")
#     exit()
# except pd.errors.EmptyDataError:
#     print("Error: CSV file is empty")
#     exit()

'''Tasks:
    2. Calculate: total, average, grade (A+/A/B/C/F), rank for each student.'''

# Calculate Total & Average

# print(df.head())
# print(df.columns)

subjects = ['Maths', 'Science', 'English', 'Computer','History']

df['Total'] = df[subjects].sum(axis=1)
df['Average'] = df[subjects].mean(axis=1)

# print(df['Total'])
# print(df['Average'])
    
# Now we calculate grade of eaach students. 

def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "F"
    
    
df['Grade'] = df['Average'].apply(calculate_grade)

# print(df['Grade'])
# print(df)

#Rank Calculation

df['Rank'] = df['Total'].rank(
    ascending=False,
    method='min'
).astype(int)


# print(df['Rank'])

# print(df)

# The 3rd and 18th ranks were secured by two students each. Therefore, ranks 4 and 19 are not assigned and do not appear in the table.

''' Tasks:
     3. Summary statistics: class average, topper, failure rate, city-wise breakdown.'''

# Summary Statistics :

class_avarage = df['Average'].mean()


topper = df.loc[df['Total'].idxmax()]
# loc[] is used to access rows by their index label.
# topper : 11    Anjali   19   Gwalior     95       94       96        98       97            8    480     96.0    A+     1

# print('Class Avarage :',class_avarage)
# print('Topper of the class :', topper)



# Failure rate

failure_rate = (
    len(df[df['Grade'] == 'f'])/len(df)
)*100

# print(failure_rate)      #0.0

# The failure rate is 0.0% because no students met the failure criteria in the dataset.

City_summery = (
    df.groupby('City')['Average'].mean().round(2)
)

# print(City_summery)




print("===== SUMMARY =====")

print(f"Class Average: {class_avarage :.2f}")

print(
    f"Topper: {topper['Name']} "
    f"({topper['Total']} marks)"
)

print(
    f"Failure Rate: "
    f"{failure_rate:.2f}%"
)

print("\nCity Wise Average")
print(City_summery)