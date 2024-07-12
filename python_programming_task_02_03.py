import pandas as pd
# Example DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Boston'],
    'Salary': [60000, 80000, 70000, 90000, 75000]
}
df = pd.DataFrame(data)
# Filter rows based on a condition
# Example: Selecting people older than 30
filtered_df = df[df['Age'] > 30]
print("Filtered Data:")
print(filtered_df)
# Group by a column and perform aggregation
# Example: Group by City and calculate average Salary
grouped_df = df.groupby('City').agg({'Salary': 'mean', 'Age': 'median'}).reset_index()
print("\nGrouped Data:")
print(grouped_df)