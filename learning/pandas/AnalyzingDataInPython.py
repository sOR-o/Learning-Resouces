import pandas as pd

# Reading data from a CSV file
df = pd.read_csv("your_input_csv_file.csv")

# Getting the data types of each column
column_data_types = df.dtypes

# Getting summary statistics for numeric columns
summary_statistics_numeric = df.describe()

# Getting summary statistics for all columns, including non-numeric ones
summary_statistics_all = df.describe(include="all")

# Getting information about the DataFrame, including non-null values and memory usage
data_info = df.info()

# Printing the data types of each column
print("Data Types of Each Column:")
print(column_data_types)

# Printing summary statistics for numeric columns
print("\nSummary Statistics for Numeric Columns:")
print(summary_statistics_numeric)

# Printing summary statistics for all columns
print("\nSummary Statistics for All Columns:")
print(summary_statistics_all)

# Printing DataFrame info, including non-null values and memory usage
print("\nDataFrame Info:")
print(data_info)
