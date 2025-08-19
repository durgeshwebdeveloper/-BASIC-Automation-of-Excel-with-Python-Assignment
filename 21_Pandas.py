 # Pandas Data Structures 
# 1. Create  a Series from a list of integers.
import pandas as pd 
s = pd.Series([10,20,30,40])
print(s)
# Output: 
# 0    10
# 1    20
# 2    30
# 3    40
# dtype: int64

# 2. Create a Series from a dictionary.
data = {'a': 100, "b": 200, 'c':300}
s = pd.Series(data)
print(s)
# Output:
# a    100
# b    200
# c    300
# dtype: int64

# 3. Creates a Series from a NumPy array.
import numpy as np 
arr = np.array([1,2,3])
s = pd.Series(arr)
print(s)
# Output:
# 0    1
# 1    2
# 2    3
# dtype: int64'

# 4. Access the first and last element in a Series
print(s.iloc[0], s.iloc[-1]) # Output: 1 3

# 5. Modify a value in Series by index.
s['b'] = 250
print(s)
# Outptu: 
# 0      1
# 1      2
# 2      3
# b    250
# dtype: int64

# 6. Create a DataFrame from a list of dictionary.
data  = [{'name':'Durgesh', 'age':34}, {'name':'Anoop', 'age':36}]
df = pd.DataFrame(data)
print(df)
# Output: 
#       name  age
# 0  Durgesh   34
# 1    Anoop   36

# 7. Create  a DataFrame from dictionary of lists.
data  = {'name': ['Durgesh', 'Anoop'], 'age':[23,34]}
df  = pd.DataFrame(data)
print(df)
# Output:
#      name  age
# 0  Durgesh   23
# 1    Anoop   34

# 8. Access a specific column in a DataFrame.
print(df['name'])
# Output: 
# 0    Durgesh
# 1      Anoop
# Name: name, dtype: object

# 9. Access the first row using .iloc.
print(df.iloc[0])
# Output: 
# name    Durgesh
# age          23
# Name: 0, dtype: object

# 10. Rename column 'age' to 'years'.
df.rename(columns = {'age': 'years'}, inplace = True)
print(df)
# Output: 
#       name  years
# 0  Durgesh     23
# 1    Anoop     34

  #  INDEXING AND SELECTING DATA 
# 11. Use .loc[] to access by position. 
df.index = ['row1', 'row2']
print(df.loc['row1'])
# Output: 
# name     Durgesh
# years         23
# Name: row1, dtype: object

# 12. Use .ilo[] to access by position.
print(df.iloc[1])
# Output:
# name     Anoop
# years       34
# Name: row2, dtype: object

# 13. Filter rows where age > 25.
print(df[df['years'] > 25])
# Output: 
#        name  years
# row2  Anoop     34

# 14. Create MultiIndex  DataFrame. 
arrays = [['A', 'A','B',], [1,2,1]]
index = pd.MultiIndex.from_arrays(arrays, names  = ('letters', 'number'))
df = pd.DataFrame({'value':[10,20,30]}, index = index)
print(df)
# Output: 
# letters number
# A       1          10
#         2          20
# B       1          30

    # DATA IMPORT AND EXPORT 
# 15. Read a CSV file.
import pandas as pd
df =pd.read_csv("data.csv")
print(df.head())
# Output:
#    Duration  Pulse  Maxpulse  Calories
# 0        60    110       130     409.1
# 1        60    117       145     479.0
# 2        60    103       135     340.0
# 3        45    109       175     282.4
# 4        45    117       148     406.0

# 16. Read an excel file.
# import pandas as pd
# df = pd.read_excel('data.xlsx')
# print(df)

# # 17. Export DataFrame to CSV 
df.to_csv('output.csv', index = False)
print(df)

# # 18. Export DataFrame to JSON.
df.to_json('output.json')
print(df)

#    # DATA CLEANING AND PREPROCESSING 
# # 19. Detect missing values. 
print(df.isnull())

# # 20. Drop rows with missing values.
df.dropna(inplace  = True)

# # 21. Fill missing values with zero. 
df.fillna(0, inplace = True)

# # 22. Interpolate missing values.
df.interpolate(inplace = True)

# # 23. Find duplicate rows. 
print(df.duplicated())

# # 24. Remove duplicate rows.
df.drop_duplicates(inplace=True)

#    # DATA TYPE CONVERSION 
# # 25. Convert column to integer.
df['years']  = df['years'].astype(df['date'])

# # 26. Convert string date to datetime.
df['date'] = pd.to_datetime(df['datetime'])

#     # STRING MANIPULATION 
# # 27. Convert strings to lowercase.
df['name']  = df['name'].str.lower()

# # 28. Replace substrings in column.
df['name'] = df['name'].str.replace('a', 'a')

#     #  RENAMING AND REPLACING DATA 
# # 29. Rename index labels.
df.rename(index = {'rows1':'first'},inplace = True)

# # 30. Replace values in DataFrame.
df.replace(25,26, inplace = True)

#     # DATA TRANSFORMATION
# # 31. Sort by column 'years'. 
df.sort_values(by = 'years', inplace = True)

# # 32. Group by 'name' and calculate mean.
print(df.groupby('name')['years'].mean())

# # 33. Apply sum to each group. 
print(df.groupby('name')['years'].sum())

# # 34. Apply custom function to group. 
print(df.groupby('name')['years'].agg(lambda x : max(x) - min(x)))

#             # PIVOT TABLE 
# # 35. Create  pivot table.
import pandas as pd
df =pd.read_csv("data.csv")
pivot  = df.pivot_table(index = 'name', values = 'years', aggfunc = 'mean')
print(pivot)

# 36. Multile aggregation in pivot. 
pivot = df.pivot_table(index= 'name', values = 'years', aggregation  = ['mean', 'sum'])
print(pivot)

      # APPLYING FUNCTIONS TO DATA 
# 37. Use apply() with lambda. 
df['double_age'] = df['years'].apply(lambda x : x*2)

# 38. Use .map() to convert values.
df['gender'] = df['gender'].map({'M': 'Male', 'F': 'Female'})

# 39. Use .applymap() on whole DataFrame.
print(df.applymap(str))

      # MERGING , JOINING , CONCATENATION 
# 40. Merge two DataFrames.
df1 = pd.DataFrame({'id': [1,2], 'name': ['A', 'B']})
df2  = pd.DataFrame({'id':[1,2], 'score':[90,80]})
merged = pd.merge(df1, df2, on = 'id')
print(merged)

# 41. Left join DataFrames.
merged = pd.merge(df1, df2, on = 'id', how = 'left')

# 42. Concatenate DataFrames vertically.
df_concat = pd.concat([df1, df2], axis = 0)

# 43. Use .join() on index. 
df1.set_index('id', inplace = True)
df2.set_index('id', inplace= True)
print(df1. join(df2))

          # HANDLING DATA AND TIME 
# 44. Convert column to datetime. 
df['dob'] = pd.to_datetime(df['dob'])

# 45. Extract year from datetime.
df['year'] = df['dob'].dt.year

# 46. Filter rows by year.
print(df['dob'].dt.year == 2020)

# 47. Create a time series index. 
date_rng = pd.date_range(start  = '2020-01-01', periods = 5, freq = 'D')
df = pd.DataFrame(date_rng,columns = ['data'])
df.set_index('date', inplace= True)
print(df)

# 48. Resample by month and count entries.
df.resample('M').count()

# 49. Add 7 days to a datetime column.
df['nest_week'] = df['dob'] + pd.Timedelta(days = 7)

# 50. Calculate age from DOB. 
today = pd.to_datetime('today')
df['age'] = (today-df['dob']).dt.days//365