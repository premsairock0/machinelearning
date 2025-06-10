import pandas as pd

def candidate_elimination(filename):
    # Read the CSV data
    data = pd.read_csv(filename)
    concepts = data.iloc[:, :-1].values
    target = data.iloc[:, -1].values

    # Initialize specific hypothesis S
    s = list(concepts[0])
    
    # Initialize general hypothesis G
    g = [['?' for _ in range(len(s))] for _ in range(len(s))]

    for i, instance in enumerate(concepts):
        if target[i] == "Yes":
            for j in range(len(s)):
                if s[j] != instance[j]:
                    s[j] = '?'
                    g[j][j] = '?'
        else:  # If the example is negative
            for j in range(len(s)):
                if s[j] != instance[j]:
                    g[j][j] = s[j]
                else:
                    g[j][j] = '?'

    # Remove empty hypotheses
    g = [hypo for hypo in g if hypo != ['?' for _ in range(len(s))]]

    print("Final Specific Hypothesis (S):", s)
    print("Final General Hypotheses (G):", g)

# Run the algorithm
candidate_elimination("finds.csv")