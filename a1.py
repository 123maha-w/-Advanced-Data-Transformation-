import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Titanic Dataset.csv')

data.head(5)

minimum_age = data['Age'].min()
print('minimum age :',minimum_age)

maximum_age = data['Age'].max()
print('maximum age :',maximum_age)

bins = [0, 15, 30, 45, 60, 75]

data['binned_age'] = pd.cut(data['Age'],bins)

print(data[['binned_age','Age']].head())

age_labels = ['Young','Young - Adult','Middle Aged','Middle-Older Aged','Senior']

data['binned_age'] = pd.cut(data['Age'], bins,labels = age_labels)

data['binned_age'].value_counts().plot(kind='bar')

plt.title('dance class age distribution')
plt.xlabel('Ages')
plt.ylabel('count')

labels = ['PassengerId','Survied','Pclass','Age','SibSp','Parch','Fare']

for label in labels:
    print('distribution of', label)
    sns.distplot(data[label])
    plt.show()
    print('skewness - ',data[label].skew())


data['SibSp'] = np.log(data['SibSp'])
data['Parch'] = np.log(data['Parch'])
data['Fare'] = np.log(data['Fare'])