import pandas as pd

# Sample DataFrame with numerical data
data = {
    'Age': [25, 30, 35, 40, 45],
    'Income': [45000, 55000, 60000, 70000, 80000],
    'Temperature(C)': [20, 25, 30, 35, 40]
}
df = pd.DataFrame(data)

# Min-Max Scaling
# Scale the data to the range [0, 1]
df_min_max = (df - df.min()) / (df.max() - df.min())

# Z-Score Scaling (Standardization)
# Standardize the data to have a mean of 0 and a standard deviation of 1
df_z_score = (df - df.mean()) / df.std()

# Scaling by a Custom Range
# Scale the data to a custom range [0, 100]
custom_range = 100
df_custom_range = (df - df.min()) / (df.max() - df.min()) * custom_range

# Scaling by Dividing by Max Value
# Scale the data by dividing each value by the maximum value in the column
df_divided_by_max = df / df.max()

# Display the normalized DataFrames
print("Original DataFrame:")
print(df)

print("\nMin-Max Scaled DataFrame:")
print(df_min_max)

print("\nZ-Score Scaled DataFrame:")
print(df_z_score)

print("\nCustom Range Scaled DataFrame:")
print(df_custom_range)

print("\nDivided by Max Scaled DataFrame:")
print(df_divided_by_max)
