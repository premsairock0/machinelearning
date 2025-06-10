from sklearn import tree
import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_csv("id3gini.csv")

x = data.iloc[:,:-1]
y = data.iloc[:,-1]

x = pd.get_dummies(x)

model = tree.DecisionTreeClassifier(criterion="gini").fit(x,y)
tree.plot_tree(model,feature_names=x.columns)
plt.show()

