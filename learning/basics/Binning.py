import pandas as pd
import numpy as np

# Sample DataFrame with a "price" column
data = {
    'Car': ['Toyota', 'Honda', 'Ford', 'Chevrolet'],
    'Price': [15000, 25000, 30000, 45000]
}
df = pd.DataFrame(data)

# Define bin edges using np.linspace
bins = np.linspace(min(df["Price"]), max(df["Price"]), 4)

# Define labels for the bins
group_names = ["Low", "Medium", "High"]

# Create a new column "price-binned" using pd.cut
df["price-binned"] = pd.cut(df["Price"], bins, labels=group_names, include_lowest=True)
