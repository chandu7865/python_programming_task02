import pandas as pd

# Example DataFrame with missing values
data = {
    'A': [1, 2, None, 4],
    'B': [5, None, 7, 8],
    'C': ['x', 'y', 'z', None]
}
df = pd.DataFrame(data)
# Check for missing values
print(df.isnull())
# Drop rows with any missing values
df.dropna(inplace=True)
# Fill missing values in column 'A' with the mean of column 'A'
df['A'].fillna(df['A'].mean(), inplace=True)
# Fill missing values in column 'B' with a specific value
df['B'].fillna(0, inplace=True)
# Example DataFrame with duplicates
data = {
    'A': [1, 2, 2, 3, 4],
    'B': ['x', 'y', 'y', 'z', 'z']
}
df = pd.DataFrame(data)
# Identify duplicates
print("Duplicate rows:")
print(df[df.duplicated()])
# Remove duplicates
df.drop_duplicates(inplace=True)
# Print cleaned DataFrame
print("DataFrame after removing duplicates:")
print(df)
