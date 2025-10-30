import pandas as pd

data = {'Name': ['Aditi', 'Rohan', 'Neha'],'Age': [18, 19, 18],'Marks': [85, 78, 92]}

df = pd.DataFrame(data)
df = pd.read_csv('student.csv')

# print(df)


print(df.head())       # shows first 5 rows
print(df.info())       # shows column names, data types, and nulls
print(df.describe())   # quick statistics for numeric columns
