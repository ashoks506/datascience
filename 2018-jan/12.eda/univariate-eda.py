import os
import pandas as pd
#import matplotlib.pyplot as plt
import seaborn as sns

#changes working directory
#os.chdir("D:/titanic")
print(os.getcwd())
os.chdir('D:\Projects\datasets')
titanic_train = pd.read_csv("titanic_train.csv")

#EDA
titanic_train.shape
titanic_train.info()

#numerical summary of continuous columns
titanic_train.describe()
titanic_train['Age'].describe()

#categorical columns: statistical EDA
pd.crosstab(index=titanic_train["Survived"], columns="count")
pd.crosstab(index=titanic_train["Pclass"], columns="count")  
pd.crosstab(index=titanic_train["Sex"],  columns="count")

#categorical columns: visual EDA
sns.countplot(x='Survived',data=titanic_train)
sns.countplot(x='Pclass',data=titanic_train)
sns.countplot(x='Sex',data=titanic_train)

#continuous features: statistical EDA
titanic_train['Fare'].describe()

#continuous features: visual EDA
sns.boxplot(x='Fare',data=titanic_train)
sns.distplot(titanic_train['Fare'])
sns.distplot(titanic_train['Fare'], kde=False)
sns.distplot(titanic_train['Fare'], bins=20, rug=True, kde=False)
sns.distplot(titanic_train['Fare'], bins=100, kde=False)


#continuous features: statistical EDA
titanic_train['Age'].describe()
sns.boxplot(x='Age',data=titanic_train)
#here kde is default no need to specifie if specifie no problem
sns.distplot(titanic_train['Age'], kde=True)

