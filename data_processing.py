from ucimlrepo import fetch_ucirepo 
import pandas as pd
  

def frequency_tables(X):
<<<<<<< Updated upstream
    sex_freq = X['sex'].value_counts()
    age_groups = [14,16,19,22]
    age_labels = ['15-16', '17-19', '20-22']
=======
    df = pd.concat([X, y], axis=1)
>>>>>>> Stashed changes

    # Generate frequency table for sex
    sex_freq = df.groupby('sex')[['G1', 'G2', 'G3']].count()

    # Define age groups properly
    age_groups = [14, 17, df['age'].max() + 1]  # Ensure all ages are covered
    age_labels = ['15-17', '18-22']
    df['age_group'] = pd.cut(df['age'], bins=age_groups, labels=age_labels, right=False)

    # Generate frequency table for age groups
    age_freq = df.groupby('age_group')[['G1', 'G2', 'G3']].count()

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