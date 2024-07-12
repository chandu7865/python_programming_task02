import pandas as pd
# Load CSV file into a DataFrame
df = pd.read_csv('your_file.csv')
# Display the first few rows of the DataFrame
print(df.head())# Display first few rows
print(df.head())
# Display last few rows
print(df.tail())# Access a single column
column = df['column_name']
# Access multiple columns
subset = df[['column1', 'column2']]
# Sort DataFrame by a column
sorted_df = df.sort_values(by='column_name')
# Filter rows based on a condition
filtered_data = df[df['column_name'] > 10]
# Add a new column
df['new_column'] = some_values
# Remove a column
df = df.drop(columns=['column_to_drop'])
# Save DataFrame to CSV
df.to_csv('output_file.csv', index=False)
# Check for missing values
print(df.isnull().sum())
# Drop rows with any NaN values
df = df.dropna()
# Fill NaN values with a specific value
df['column_name'].fillna(value, inplace=True)