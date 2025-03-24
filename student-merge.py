import pandas as pd

# Read the CSV files
d1 = pd.read_csv("student-mat.csv", sep=";")
d2 = pd.read_csv("student-por.csv", sep=";")

# Merge the datasets on the specified columns
d3 = pd.merge(d1, d2, on=["school", "sex", "age", "address", "famsize", "Pstatus", 
                            "Medu", "Fedu", "Mjob", "Fjob", "reason", "nursery", "internet"])

# Print the number of rows
print(len(d3))  # Expected output: 382 students

# Print the number of unique rows
print(d2.drop_duplicates().shape[0])