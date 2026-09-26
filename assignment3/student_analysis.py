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


# question 7

# Display the total number of missing values in each column.

print(df.isnull().sum())

# Fill the missing marks with the mean of the respective subject using inplace=True.


# df["English"].fillna(df["English"].mean())
# df["Maths"].fillna(df["Maths"].mean())
# df["Science"].fillna(df["Science"].mean())


# print(df.isnull().sum())

df.fillna(
    {
        "English": df["English"].mean(),
        "Maths": df["Maths"].mean(),
        "Science": df["Science"].mean(),
    },
    inplace=True,
)

print(df)
print(df[["English", "Maths", "Science"]].isnull().sum())

# Handle any remaining missing values in other columns appropriately.

print(df.isnull().sum())
# Display the total number of missing values in each column again to verify that the missing values have been handled.

print(df.isnull().sum())

# question 8

print(df[df["Gender"] == "female"])

# question 9

print(df[df["Catogory"].isin(["a", "c"])])

# question 10
