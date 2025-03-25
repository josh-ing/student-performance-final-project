from ucimlrepo import fetch_ucirepo 
import pandas as pd
import matplotlib.pyplot as plt
  

def frequency_tables(X):
    sex_freq = X['sex'].value_counts()
    age_groups = [14, 17, X['age'].max()]
    age_labels = ['15-17', '18+']

    X['age_group'] = pd.cut(X['age'], bins=age_groups, labels=age_labels, right=True)

    # Frequency table for age groups
    age_freq = X['age_group'].value_counts().sort_index()

    return sex_freq, age_freq

def plot_subgroups(X, y):
    df = pd.concat([X, y], axis=1)
    age_groups = [14, 17, df['age'].max()]
    age_labels = ['15-17', '18+']

    df['age_group'] = pd.cut(df['age'], bins=age_groups, labels=age_labels, right=True)

    df_long = df.melt(id_vars=['sex', 'age_group'], value_vars=['G1', 'G2', 'G3'],
                      var_name='Grade Period', value_name='Score')


    grade_labels = {
        'G1': 'First Period',
        'G2': 'Second Period',
        'G3': 'Final Grade'
    }
    df_long['Grade Period'] = df_long['Grade Period'].map(grade_labels)

    # sex
    fig, axes = plt.subplots(1, 3, figsize=(18, 5), sharey=True)
    for i, grade in enumerate(grade_labels.values()):
        sex_freq = df_long[df_long['Grade Period'] == grade].groupby(['Score', 'sex']).size().unstack(fill_value=0)
        sex_freq.columns = sex_freq.columns.map({'F': 'female', 'M': 'male'})
        sex_freq.plot(kind='bar', stacked=True, ax=axes[i])
        axes[i].set_title(f'{grade} by Sex')
        axes[i].set_xlabel('Score')
        axes[i].set_ylabel('Number of Students' if i == 0 else '')
        axes[i].legend(title='Sex')
    fig.suptitle('Grade Score Frequencies by Sex')
    plt.tight_layout()
    plt.savefig('sex_versus_score.png')

    # age
    fig, axes = plt.subplots(1, 3, figsize=(18, 5), sharey=True)
    for i, grade in enumerate(grade_labels.values()):
        age_freq = df_long[df_long['Grade Period'] == grade].groupby(['Score', 'age_group']).size().unstack(fill_value=0)
        age_freq.plot(kind='bar', stacked=True, ax=axes[i])
        axes[i].set_title(f'{grade} by Age Group')
        axes[i].set_xlabel('Score')
        axes[i].set_ylabel('Number of Students' if i == 0 else '')
        axes[i].legend(title='Age Group')
    fig.suptitle('Grade Score Frequencies by Age Group')
    plt.tight_layout()
    plt.savefig('age_group_versus_score.png')

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

    plot_subgroups(X, y)