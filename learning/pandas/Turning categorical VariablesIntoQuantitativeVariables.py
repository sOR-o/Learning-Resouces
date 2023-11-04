import pandas as pd

# Sample DataFrame with a "fuel" column
data = {
    'Car': ['Toyota', 'Honda', 'Ford', 'Chevrolet'],
    'fuel': ['Gas', 'Diesel', 'Gas', 'Electric']
}
df = pd.DataFrame(data)

# Perform one-hot encoding on the "fuel" column
fuel_dummies = pd.get_dummies(df['fuel'])

# Concatenate the one-hot encoded columns with the original DataFrame
df_encoded = pd.concat([df, fuel_dummies], axis=1)

# Drop the original "fuel" column
df_encoded.drop('fuel', axis=1, inplace=True)

# Display the DataFrame with one-hot encoded "fuel" categories
print(df_encoded)
