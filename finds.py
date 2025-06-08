import pandas as pd

def find_s(file):
    data = pd.read_csv(file)
    positives = data[data[data.columns[-1]] == 'Yes'].iloc[:, :-1]
    
    hypothesis = list(positives.iloc[0])

    for _, row in positives.iterrows():
        for i in range(len(hypothesis)):
            if hypothesis[i] != row[i]:
                hypothesis[i] = '?'
    return hypothesis

print(find_s('finds.csv'))
