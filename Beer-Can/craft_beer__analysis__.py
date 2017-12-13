
# coding: utf-8

# In[1]:


# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

from subprocess import check_output

# Any results you write to the current directory are saved as output.


# In[2]:


beer = pd.read_csv('../input/beers.csv')


# In[3]:


beer.head()


# In[4]:


beer.shape[0]


# In[5]:


beer.shape[1]


# In[6]:


nans = pd.concat([beer.isnull().sum(), beer.isnull().sum() / beer.shape[0]], axis=1, keys=['Beer', 'Percentage'])
print(nans[nans.sum(axis=1) > 0])


# In[7]:


beer['ounces'].describe()


# In[8]:


from scipy import stats
import seaborn as sns
sns.plt.figure()
sns.plt.subplot(1, 2, 1)
sns.plt.title('Beer Ounce Dist')
sns.distplot(beer.ounces, fit=stats.norm)
sns.plt.subplot(1, 2, 2)
stats.probplot(beer.ounces, plot=sns.plt)
sns.plt.show()
print("Skewness: %f" % beer.ounces.skew())
print("Kurtosis: %f" % beer.ounces.kurt())


# In[9]:


sns.distplot(beer.ounces,bins=10)


# In[10]:


beer.drop(['Unnamed: 0'],axis =1,inplace=True)


# In[11]:


beer.head()


# In[12]:


print('Null Count of ibu :',beer['ibu'].isnull().sum())
beer.ibu.describe()


# In[13]:


beer.name.describe()


# In[14]:


sns.countplot(x="name", data=beer)


# In[15]:


beer['style'].describe()


# In[16]:


beer['style'].unique()


# In[17]:


sns.countplot('ounces',data=beer)


# In[18]:


beer.abv.describe()


# In[19]:


beer.abv.isnull().sum()


# In[20]:


x = beer[pd.notnull(beer['abv'])]['abv']


# In[21]:


sns.distplot(x)


# In[22]:


sns.plt.figure()
sns.plt.subplot(1, 2, 1)
sns.plt.rcParams['figure.figsize']=(5,5)
sns.plt.title('Beer abv Dist')
sns.distplot(x, fit=stats.norm,color='blue')
sns.plt.subplot(1, 2, 2)
stats.probplot(x, plot=sns.plt)
sns.plt.show()
print("Skewness: %f" % x.skew())
print("Kurtosis: %f" % x.kurt())


# In[23]:


print("Skewness: %f" % np.log(x).skew())
print("Kurtosis: %f" % np.log(x).kurt())


# In[24]:


print("Skewness: %f" % np.log(x**2+0.059773).skew())
print("Kurtosis: %f" % np.log(x**2+0.059773).kurt())


# In[25]:


print("Skewness: %f" % np.log(x+0.059773).skew())
print("Kurtosis: %f" % np.log(x+0.059773).kurt())


# In[26]:


print("Skewness: %f" % np.log(x+0.056).skew())
print("Kurtosis: %f" % np.log(x+0.056).kurt())


# In[27]:


print("Skewness: %f" % np.log(x+0.015).skew())
print("Kurtosis: %f" % np.log(x+0.015).kurt())


# In[28]:


print("Skewness: %f" % np.log(x+0.02).skew())
print("Kurtosis: %f" % np.log(x+0.02).kurt())


# In[29]:


v = 0.2
fig, axs = sns.plt.subplots(ncols=2)
fig.
sns.plt.title('Beer abv Dist')
sns.distplot(np.log(x+v), fit=stats.norm,color='blue',ax=axs[0])
stats.probplot(np.log(x+v),plot=axs[1])
sns.plt.show()
print("Skewness: %f" % np.log(x+v).skew())
print("Kurtosis: %f" % np.log(x+v).kurt())


# In[30]:


import seaborn as sns
v = 0.2

sns.plt.figure()
sns.plt.subplot(1, 2, 1)
sns.plt.title('Beer abv Dist')
sns.distplot(np.log(x+v), fit=stats.norm,color='blue')
sns.plt.subplot(1, 2, 2)
stats.probplot(np.log(x+v), plot=sns.plt)
sns.plt.show()
print("Skewness: %f" % np.log(x+v).skew())
print("Kurtosis: %f" % np.log(x+v).kurt())


# In[31]:


beer['abv'] = beer['abv'].fillna(0.059773)


# In[32]:


sns.distplot(beer['abv'])


# In[33]:


corrmat = beer.corr()


# In[34]:


corrmat


# In[35]:


corrmat = beer.corr()


# In[36]:


corrmat


# In[37]:


f, ax = sns.plt.subplots(figsize=(12, 9))
sns.heatmap(corrmat, vmax=.8, square=True)
sns.plt.yticks(rotation=0)
sns.plt.xticks(rotation=90)
sns.plt.show()


# In[38]:


ibu_train = beer[pd.notnull(beer['ibu'])]
ibu_test = beer[pd.isnull(beer['ibu'])]


# In[39]:


from sklearn import  linear_model
from sklearn.metrics import mean_squared_error, r2_score

regr = linear_model.LinearRegression()
x_train = np.array(ibu_train['abv'])
y_train = np.array(ibu_train['ibu'])
x_test = np.array(ibu_test['abv'])


# In[40]:


regr.fit(x_train.reshape(-1,1),y_train.reshape(-1,1))


# In[41]:


y_test = regr.predict(x_test.reshape(-1,1))


# In[42]:


ibu_test['ibu'] = y_test


# In[43]:


ibu_train


# In[44]:


ibu_test


# In[45]:


type(ibu_test)


# In[46]:


beer = pd.concat([ibu_test,ibu_train], axis=0)


# In[47]:


beer.head()


# In[48]:


sns.distplot(beer['ibu'],fit=stats.norm,color='yellow')
print("Skewness: %f" %beer['ibu'].skew())
print("Kurtosis: %f" %beer['ibu'].kurt())


# In[49]:




