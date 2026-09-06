import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Titanic Dataset.csv')

data.head(5)

sns.boxplot(data=data,x='Embarked',y='Age')
plt.show()

plt.scatter(x=data['Fare'],y=data['Survied'])
plt.ylabel('Survied')
plt.xlabel('Fare')
plt.show()


plt.scatter(x=data['Parch'],y=data['Survied'])
plt.ylabel('Survied')
plt.xlabel('Parch')
plt.show()


plt.scatter(x=data['SibSp'],y=data['Survied'])
plt.ylabel('Survied')
plt.xlabel('SibSp')
plt.show()


association_categorical = pd.crosstab(data['Gender'],data['Embarked'])
print(association_categorical)