# Number of Unique Subjects Taught by Each Teacher

import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df = teacher.groupby('teacher_id').nunique('subject_id').reset_index()
    df = df[['teacher_id', 'subject_id']].rename(columns={'subject_id': "cnt"})
    print(df)
    return df

data = [[1, 2, 3], [1, 2, 4], [1, 3, 3], [2, 1, 1], [2, 2, 1], [2, 3, 1], [2, 4, 1]]
teacher = pd.DataFrame(data, columns=['teacher_id', 'subject_id', 'dept_id']).astype({'teacher_id':'Int64', 'subject_id':'Int64', 'dept_id':'Int64'})
count_unique_subjects(teacher)