from sklearn.linear_model import LinearRegression

def perform_linear_regression(df):
    """
    Perform simple linear regression on the given DataFrame.

    Parameters:
    - df (pd.DataFrame): Input DataFrame with columns 'highway-mpg' and 'price'.

    Returns:
    - lm (LinearRegression): Fitted linear regression model.
    - X (pd.DataFrame): Input features.
    - Y (pd.Series): Target variable.
    - y_pred (numpy.ndarray): Predictions based on the input features.
    """

    # Creating a linear regression model
    lm = LinearRegression()

    # Extracting the input features and target variable
    X = df[['highway-mpg']]
    Y = df['price']

    # Fitting the model to the data
    lm.fit(X, Y)

    # Making predictions
    y_pred = lm.predict(X)

    # Outputting the coefficients and intercept
    print("Coefficients:", lm.coef_)
    print("Intercept:", lm.intercept_)

    return lm, X, Y, y_pred

# Example usage with a DataFrame named 'df'
# Ensure 'df' contains columns 'highway-mpg' and 'price'
# df = ...

# Call the function
linear_regression_model, X, Y, y_pred = perform_linear_regression(df)
