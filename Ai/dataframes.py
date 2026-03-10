import pandas as pd

coffee = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv')

# print(coffee.head(3))  # first 3 elements

# print(coffee.tail(3)) # last 3 elements

# print(coffee.sample(3)) # any 3 random elements

# print(coffee.loc[3]) # access any row and column
# print(coffee.loc[2:6])
# print(coffee.loc[1:5, "Day"]) # accessed only one column named Day from 1th index to 5th index
# print(coffee.loc[1:5, ["Day", "Units Sold"]]) # accessd column day and units sold from 1th to 5th index

# print(coffee.iloc[1:3, 1]) # similar to loc but it taked index value for columns instead of column_name

# print(coffee.at[0, "Units Sold"]) # similar to loc but it is used to access only one value (can't access multiple value)
# print(coffee.iat[0, 1]) # similar to iloc but it is used to access only one value (can't access multiple value)

## Modify data
# print(coffee.loc[1])
# coffee.loc[1, "Unit Sold"] = 10
# print(coffee.loc[1]) # value changed for row 1 column_name unit sold to 10

# # sort value 
print(coffee.sort_values("Day")) # ascending order with respect to coulmn_name = day
print(coffee.sort_values("Day", ascending=False)) # descending order with respect to coulmn_name = day
print(coffee.sort_index(["Day", "Units Sold"])) 