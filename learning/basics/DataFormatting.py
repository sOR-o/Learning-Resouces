import pandas as pd

# Sample DataFrame
data = {
    'make': ['Toyota', 'Honda', 'Ford', 'Chevrolet'],
    'city-mpg': [22, 30, 27, 25]
}
df = pd.DataFrame(data)

# Calculate a new column by performing a calculation on an existing column
df['city-L/100km'] = 235 / df['city-mpg']

# Rename a column
df.rename(columns={'city-mpg': 'city-mpg (original)'}, inplace=True)

# Print the modified DataFrame
print("Modified DataFrame:")
print(df)

# Sample DataFrame with "price" column as strings
data = {
    'Car': ['Toyota', 'Honda', 'Ford', 'Chevrolet'],
    'Price': ['$22,000', '$30,500', '$27,800', '$25,600']
}
df = pd.DataFrame(data)

# Display the initial DataFrame
print("Initial DataFrame:")
print(df)

# Convert the "Price" column to float
df[["Price"]] = df[["Price"]].replace('[\$,]', '', regex=True).astype("float")

# Perform a numerical operation (e.g., calculate the average price)
average_price = df["Price"].mean()

# Display the modified DataFrame and the average price
print("\nModified DataFrame with 'Price' as float:")
print(df)
print(f"\nAverage Price: ${average_price:.2f}")

