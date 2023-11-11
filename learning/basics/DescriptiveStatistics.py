import pandas as pd
import matplotlib.pyplot as plt

# Create a sample DataFrame
data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'A'],
    'Values': [10, 20, 25, 30, 40, 50]
}
df = pd.DataFrame(data)

# Use .value_counts() to get the frequency distribution of 'Category'
value_counts = df['Category'].value_counts()
print("Value Counts (Frequency Distribution of 'Category'):")
print(value_counts)

# Use .boxplot() to create a boxplot of the 'Values' column
df.boxplot(column='Values')
plt.title('Boxplot of Values')
plt.show()

# Create a scatter plot of 'Category' vs 'Values'
plt.scatter(df['Category'], df['Values'])
plt.xlabel('Category')
plt.ylabel('Values')
plt.title('Scatter Plot of Category vs Values')
plt.show()
