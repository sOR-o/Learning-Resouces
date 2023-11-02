import pandas as pd
import numpy as np

# Sample dataset
data = {'Age': [25, 30, np.nan, 35, 40],
        'Income': ['$40,000', '$50,000', '$60,000', '$70,000', '$80,000'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
        'Score': [85, 92, 75, 88, 94]}
df = pd.DataFrame(data)

# Check with the data collection source for missing values
# It's important to understand why data is missing and whether it can be collected.

# Drop the missing values
# If missing values cannot be collected, you can drop them from the dataset.

# Drop the variable (column) with missing values
df.dropna(subset=['Age'], inplace=True)

# Drop the data entry (row) with missing values
# df.dropna(axis=0, inplace=True)

# Replace the missing values
# If you decide to replace missing values, you have several options.

# Replace with the mean (average) of similar datapoints
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Replace it by frequency (mode)
# df['Age'].fillna(df['Age'].mode()[0], inplace=True)

# Replace it based on other functions or data-driven methods

# Leave it as missing data
# If you have a good reason to leave missing data, you can do so.

data = {'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)

# Using inplace=True to modify the original DataFrame
df.drop(columns='A', inplace=True)
# The 'A' column is removed from the original DataFrame 'df'

# Using inplace=False (or not specifying) to create a new DataFrame
new_df = df.drop(columns='B', inplace=False)
# A new DataFrame 'new_df' is created with 'B' removed, while the original 'df' remains unchanged

# df and new_df now have different contents

data = {'A': [1, 2, 3, 4, 5],
        'B': ['apple', 'banana', 'cherry', 'apple', 'date']}

df = pd.DataFrame(data)

# Replace 'apple' with 'orange' in column 'B'
df['B'].replace('apple', 'orange', inplace=True)

# Replace multiple values in column 'A'
df['A'].replace([1, 3], [10, 30], inplace=True)

# Replace using a dictionary
replace_dict = {'banana': 'grape', 'date': 'fig'}
df['B'].replace(replace_dict, inplace=True)

print(df)

# Sample DataFrame with a "normalized-losses" column containing missing values (np.nan)
data = {'normalized-losses': [140, 160, np.nan, 120, np.nan, 95, 100, 98]}
df = pd.DataFrame(data)

# Calculate the mean of the "normalized-losses" column
mean = df["normalized-losses"].mean()

# Replace missing values in the "normalized-losses" column with the mean
df["normalized-losses"].replace(np.nan, mean, inplace=True)

# Print the modified DataFrame
print("Modified DataFrame:")
print(df)
