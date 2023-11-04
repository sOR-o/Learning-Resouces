import numpy as np
from scipy import stats

def calculate_pearson_correlation(x, y):
    """
    Calculate the Pearson correlation coefficient and p-value between two sets of data.

    Parameters:
    x (array-like): First set of data.
    y (array-like): Second set of data.

    Returns:
    correlation_coefficient (float): The Pearson correlation coefficient.
    p_value (float): The p-value for testing non-correlation.

    Docstring Explanations:
    - Measure the strength of the correlation between two features.
    - Correlation coefficient:
        - Close to +1: Large Positive relationship
        - Close to -1: Large Negative relationship
        - Close to 0: No relationship
    - P-value:
        - P-value < 0.001: Strong certainty in the result
        - P-value < 0.05: Moderate certainty in the result
        - P-value < 0.1: Weak certainty in the result
        - P-value > 0.1: No certainty in the result
    - Strong Correlation:
        - Correlation coefficient close to 1 or -1
        - P value less than 0.001
    """

    # Calculate the Pearson correlation coefficient and p-value
    correlation_coefficient, p_value = stats.pearsonr(x, y)

    return correlation_coefficient, p_value

# Sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 6])

# Calculate the Pearson correlation coefficient and p-value
correlation_coefficient, p_value = calculate_pearson_correlation(x, y)

print("Pearson Correlation Coefficient:", correlation_coefficient)
print("P-value:", p_value)

if p_value < 0.05:
    print("There is a significant correlation.")
else:
    print("There is no significant correlation.")
