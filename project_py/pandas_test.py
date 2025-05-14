import pandas as pd

# Create a DataFrame directly
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Salary': [70000, 80000, 120000, 90000]
}
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Basic operations
print("\nBasic Info:")
print(df.info())  # Information about the DataFrame

print("\nSummary Statistics:")
print(df.describe())  # Summary statistics for numerical columns

# Selecting data
print("\nSelecting a Column:")
print(df['Name'])  # Select a single column

print("\nSelecting Multiple Columns:")
print(df[['Name', 'City']])  # Select multiple columns

print("\nSelecting Rows by Index:")
print(df.iloc[1])  # Select the second row (index 1)

print("\nSelecting Rows by Condition:")
print(df[df['Age'] > 30])  # Filter rows where Age > 30

# Adding a new column
df['Bonus'] = df['Salary'] * 0.1
print("\nDataFrame with Bonus Column:")
print(df)

# Grouping and aggregation
print("\nGrouping by City and Calculating Mean Salary:")
print(df.groupby('City')['Salary'].mean())

# Sorting
print("\nSorting by Age:")
print(df.sort_values(by='Age'))

# Handling missing data
df.loc[2, 'Salary'] = None  # Introduce a missing value
print("\nDataFrame with Missing Value:")
print(df)

print("\nFilling Missing Values:")
print(df.fillna(0))  # Fill missing values with 0

print("\nDropping Rows with Missing Values:")
print(df.dropna())  # Drop rows with missing values

# Exporting to CSV
df.to_csv('output.csv', index=False)
print("\nDataFrame exported to 'output.csv'")