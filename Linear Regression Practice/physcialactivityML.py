#%%
##Imports
#%#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# %%
#Reading data into DataFrame and displaying it
df = pd.read_csv('NutritionData.csv')
df.info()
df.head()

# %%
##Drop unneccessary tables
df.drop(['Low_Confidence_Limit','High_Confidence_Limit ','YearEnd','Topic','Class','Datasource','Data_Value_Unit','QuestionID','ClassID','TopicID','DataValueTypeID','Data_Value_Type','Data_Value_Footnote_Symbol','Data_Value_Footnote','StratificationCategoryId1','StratificationID1'],axis=1,inplace=True)
df.info()

#%%
df.info()
# %%
#Create new data frames to separate by gender,education level, and income
dfgend= df[(df['Stratification1']=='Male')|(df['Stratification1']=='Female')]
dfedu = df[df['StratificationCategory1']=='Education']
dfinc = df[df['StratificationCategory1']=='Income']

dfgend.reset_index(drop=True)
dfedu.reset_index(drop=True)
dfinc.reset_index(drop=True)

# %%
##Some Visualizations of the data so far
plt.figure(figsize=(14,4))
gendcount = sns.countplot(data=dfgend,x='Question',hue='Stratification1')
gendcount.set_xticklabels(gendcount.get_xticklabels(), rotation=40, ha="right")
plt.tight_layout()
plt.title('Lifestyle 1 by Gender')
plt.show()



# %%
plt.figure(figsize=(14,4))
educount = sns.countplot(data=dfedu,x='Question',hue='Education')
educount.set_xticklabels(educount.get_xticklabels(), rotation=40, ha="right")
plt.tight_layout()
plt.title('Lifestyle 1 by Education')
plt.show()
# %%
dfedu.info()
# %%
