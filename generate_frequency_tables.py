import pandas as pd
from tabulate import tabulate

def generate_frequency_tables(input_file):
    # load dataset
    df = pd.read_excel(input_file)

    # bucket the age into two groups: 15 to 17 and 18 to 22
    df['age_group'] = pd.cut(df['age'], bins=[14, 17, 22], labels=['15-17', '18-22'], right=True)

    # define protected classes and dependent variables
    protected_classes = ['sex', 'age_group']
    dependent_variables = ['G1', 'G2', 'G3']

    # create frequency tables for each combo of protected class and dependent variable
    for protected_class in protected_classes:
        print(f"\nFrequency table for {protected_class}:")
        for dep_var in dependent_variables:
            # Generate the frequency table
            freq_table = pd.crosstab(df[protected_class], df[dep_var], margins=True)
            
            # Format the frequency table with tabulate and add vertical and horizontal lines
            print(f"\n{protected_class} vs {dep_var}:\n")
            print(tabulate(freq_table, headers='keys', tablefmt='grid', showindex=True))

file_path = "student-por.xlsx"
generate_frequency_tables(file_path)
