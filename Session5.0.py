
# coding: utf-8

# ## 1) How-to-count-distance-to-the-previous-zero
# For each value, count the difference of the distance from the previous zero (or the start
# of the Series, whichever is closer) and if there are no previous zeros,print the position
# Consider a DataFrame df where there is an integer column {'X':[7, 2, 0, 3, 4, 2, 5, 0, 3, 4]}
# The values should therefore be [1, 2, 0, 1, 2, 3, 4, 0, 1, 2]. Make this a new column 'Y'.
# import pandas as pd
# df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})

# In[2]:


import pandas as pd
import numpy as np
df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})


# In[11]:


# function to generate list to get the distence from zero in the list.
def func(lst):
    x=list(lst)
    n = None
    y = []
    for i in range(len(x)):
        if x[i] != 0 and n== None:
            y.append(i+1)
        elif x[i] == 0:
            y.append(0)
            n = 0
        else:
            n += 1
            y.append(n)
    return y


# In[12]:


# testing function
lst=[7, 2, 0, 3, 4, 2, 5, 0, 3, 4]
print(func(lst))


# In[21]:


# asssingning function return list value to df as a y column
df['Y'] = func(df['X'])


# In[28]:


df.head()


# ## 2) Create a DatetimeIndex that contains each business day of 2015 and use it to index a Series of random numbers.

# In[3]:


# Builtin funtion to get  business days in given range
bd = pd.bdate_range('2015-01-01', '2015-12-31')


# In[4]:


# geneating random int numbers of length of bd range and assining index to bd.

Df2=pd.Series(np.random.randn(len(bd)), index=bd)
#Df.columns=['Dates','Rint']
DF1=pd.DataFrame(Df2)
DF1.head()


# In[5]:


DF1.columns=['Rint']
DF1.index.names = ['index']
DF1.columns.names = ['column']


# In[6]:


DF1.head()


# ## 3) Find the sum of the values in s for every Wednesday

# In[7]:


DF1.asfreq(freq='W-WED', method='pad').sum()


# ## 4) Average For each calendar month

# In[8]:


DF1.resample('M').mean()


# ## 5) For each group of four consecutive calendar months in s, find the date on which the highest value occurred.

# In[10]:


DF1['month'] = DF1.index.month


# In[44]:


df2=DF1.loc[DF1.resample('M')['Rint'].idxmax()]


# In[157]:


df2.head()


# In[142]:


df3=df2[df2['month'].between(1, 4)]
df4=df2[df2['month'].between(5, 8)]
df5=df2[df2['month'].between(9, 12)]


# In[156]:


dc1=pd.concat([df3.where(df3['Rint']==max(df3['Rint'])),df4.where(df4['Rint']==max(df4['Rint'])),df5.where(df5['Rint']==max(df5['Rint']))])
dc1[dc1['Rint'].notna()]

