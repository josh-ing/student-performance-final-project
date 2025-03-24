from ucimlrepo import fetch_ucirepo 
import pandas as pd
  

def frequency_tables(X):
    sex_freq = X['sex'].value_counts()
    age_groups = [14,16,19,22]
    age_labels = ['15-16', '17-19', '20-22']

    X['age_group'] = pd.cut(X['age'], bins=age_groups, labels=age_labels, right=True)

    # Frequency table for age groups
    age_freq = X['age_group'].value_counts().sort_index()

    return sex_freq, age_freq

if __name__ == "__main__":
    # fetch dataset 
    student_performance = fetch_ucirepo(id=320) 
    
    # data (as pandas dataframes) 
    X = student_performance.data.features 
    y = student_performance.data.targets 
    
    # metadata 
    print(student_performance.metadata) 
    
    # variable information 
    print(student_performance.variables)
    sex_freq, age_freq = frequency_tables(X)
    print("Sex Frequency Table:")
    print(sex_freq)
    print("\nAge Group Frequency Table:")
    print(age_freq)