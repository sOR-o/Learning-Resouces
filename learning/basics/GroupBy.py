import pandas as pd

# Create a sample DataFrame
data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'A'],
    'Values': [10, 20, 25, 30, 40, 50]
}
df = pd.DataFrame(data)

# Using .groupby() for aggregation

# Group by 'Category' and calculate the mean value within each group
grouped = df.groupby('Category')['Values'].mean()
print("Using .groupby() for aggregation:")
print(grouped)

# Using .pivot() for reshaping the DataFrame

# Create a pivot table with 'Category' as columns and 'Values' as values
pivot_table = df.pivot(columns='Category', values='Values')
print("\nUsing .pivot() for reshaping the DataFrame:")
print(pivot_table)
