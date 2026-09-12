import pandas as pd

# Load the CSV file
df = pd.read_csv("student_marks.csv")

# Display the dataset
print("Student Dataset:")
print(df)

# 1. Shape of the DataFrame
print("\n1. Shape of DataFrame:")
print(df.shape)

# 2. Number of columns
print("\n2. Number of columns:")
print(len(df.columns))

# 3. Number of records / rows
print("\n3. Number of records:")
print(len(df))

# 4. Names of all columns
print("\n4. Names of all columns:")
print(df.columns)

# 5. Statistical information of numerical columns
print("\n5. Statistical information:")
print(df.describe())

# 6. Detailed information about DataFrame
print("\n6. Detailed information:")
df.info()

# 7. Type of DataFrame
print("\n7. Type of DataFrame:")
print(type(df))

# 8. Data type of one column
print("\n8. Data type of English column:")
print(df["English"].dtype)

# 9. Data types of all columns
print("\n9. Data types of all columns:")
print(df.dtypes)
