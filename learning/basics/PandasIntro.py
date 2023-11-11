import pandas as pd

# Reading a CSV file in different ways, You can read a CSV file using pd.read_csv() by providing the file path as an argument.
df = pd.read_csv("your_input_file.csv")

# Displaying the first n rows of the DataFrame
n = 5  
print(df.head(n))

# Displaying the last n rows of the DataFrame
print(df.tail(n))

# Modifying the header (column names), You can replace the default header by passing a list of column names to the 'header' parameter.
new_column_names = ["Column1", "Column2", "Column3", "Column4"]
df.columns = new_column_names

# Exporting the DataFrame to a new CSV file, You can save the DataFrame to a new CSV file using the to_csv method.
output_file_path = "new_output_file.csv"  # Replace with the desired file path
df.to_csv(output_file_path, index=False)  # Set index=False to exclude the index column in the output file
