import pandas as pd

csv_file = "student-por.csv"
excel_file = "student-por.xlsx"

# Read the CSV file
df = pd.read_csv(csv_file, sep=';')

# Save to an Excel file
df.to_excel(excel_file, index=False)

print(f"File saved as {excel_file}")
