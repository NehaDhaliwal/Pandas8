# Classes More Than 5 Students

import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby('class')['student'].count().reset_index()
    df = df[df['student'] >= 5]
    print(df[['class']])
    return df[['class']]

data = [['A', 'Math'], ['B', 'English'], ['C', 'Math'], ['D', 'Biology'], ['E', 'Math'], ['F', 'Computer'], ['G', 'Math'], ['H', 'Math'], ['I', 'Math']]
courses = pd.DataFrame(data, columns=['student', 'class']).astype({'student':'object', 'class':'object'})

find_classes(courses)