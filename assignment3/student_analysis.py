import pandas as pd

df = pd.read_csv("student_marks.CSV")

print(df)

print("Shape:", df.shape)

print("Number of columns:", df.shape[1])

print("Number of records:", df.shape[0])

print("Column names:")
print(df.columns)
print(df.describe())
df.info()
print(type(df))

# question 3

print("First 3 rows:")
print(df.head(3))

print("last 2 row:")
print(df.tail(2))

# question 4
print("Unique Gender values:")
print(df["Gender"].unique())

# Unique values in Category
print("\nUnique Category values:")
print(df["Catogory"].unique())

# question 5

print("unique value:", df["Gender"].nunique)
print("unique value:", df["scholarship"].nunique)
print("unique value:", df["Catogory"].nunique)

# question 6
print(df[["Rollno", "Name", "Science"]])
