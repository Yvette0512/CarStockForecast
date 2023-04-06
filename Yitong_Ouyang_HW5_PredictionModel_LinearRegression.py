#!/usr/bin/env python
# coding: utf-8

# # 1. Intergreating Data

# In[104]:


import sys
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import json
import csv
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.formula.api import ols
import statsmodels.formula.api as smf

#function_1: Stock Avg Price Monthly: Tesla, Ford, VolksWagen:
response = requests.get('https://api.twelvedata.com/avg?apikey=fc01582d31674d1aa5860ca3e7a5c998&interval=1month&symbol=TSLA&start_date=2018-02-01 00:00:00&format=JSON&end_date=2022-10-02 00:00:00')
data = json.loads(response.text)
my_dict2 = data['values']
df1 = pd.DataFrame.from_dict(my_dict2)
df1 = df1.loc[::-1].reset_index(drop=True)
date = pd.date_range(start='2/1/2018', end='10/1/2022', freq='MS')
df1 = df1.set_index(date)
df1 = df1.drop('datetime', axis=1)
df1.rename(columns = {'avg': 'Tesla_Stock'}, inplace = True)

#Frod:
response = requests.get("https://api.twelvedata.com/avg?apikey=fc01582d31674d1aa5860ca3e7a5c998&interval=1month&start_date=2018-02-01 00:00:00&format=JSON&end_date=2022-10-02 00:00:00&symbol=F")
data = json.loads(response.text)
my_dict2 = data['values']
df2 = pd.DataFrame.from_dict(my_dict2)
df2 = df2.loc[::-1].reset_index(drop=True)
date = pd.date_range(start='2/1/2018', end='10/1/2022', freq='MS')
df2 = df2.set_index(date)
df2 = df2.drop('datetime', axis=1)
df2.rename(columns = {'avg': 'Ford_Stock'}, inplace = True)

#VW:
response = requests.get("https://api.twelvedata.com/avg?apikey=fc01582d31674d1aa5860ca3e7a5c998&interval=1month&start_date=2018-02-01 00:00:00&format=JSON&end_date=2022-10-02 00:00:00&symbol=VWAPY")
data = json.loads(response.text)
my_dict2 = data['values']
df3 = pd.DataFrame.from_dict(my_dict2)
df3 = df3.loc[::-1].reset_index(drop=True)
date = pd.date_range(start='2/1/2018', end='10/1/2022', freq='MS')
df3 = df3.set_index(date)
df3 = df3.drop('datetime', axis=1)
df3.rename(columns = {'avg': 'VolksWagen_Stock'}, inplace = True)

df_stock_price = pd.concat([df1, df2, df3], axis="columns")
#     print(df_stock_price)

#function_2: Car Sales Monthly: Tesla, Ford, VolksWagen
#Tesla:
my_lst = list()
my_lst2 = list()
my_lst3 = list()
URL = 'https://www.goodcarbadcar.net/tesla-inc-us-sales-figures/'
content = requests.get(URL)
soup = BeautifulSoup(content.content, 'html.parser')
tags = soup.find_all('tr', id = re.compile('table_5882_row_[34567]'))
for tag in tags:
    my_lst.append(tag.get_text().replace("\n", " "))
for i in my_lst:
    x = i.split(' ')
    my_lst2 = x[2:-1]
    for i in my_lst2:
        my_lst3.append(i)
date = pd.date_range(start='2/1/2018', end='1/1/2023', freq='MS')
df1 = pd.DataFrame(my_lst3, columns =['Tesla_Sales'])
df1 = df1.set_index(date)

#Ford:
my_lst = list()
my_lst2 = list()
my_lst3 = list()
URL = 'https://www.goodcarbadcar.net/ford-us-sales-figures/'
content = requests.get(URL)
soup = BeautifulSoup(content.content, 'html.parser')
tags = soup.find_all('tr', id = re.compile(r'table_5988_row_(1[3-7])'))
for tag in tags:
    my_lst.append(tag.get_text().replace("\n", " "))
for i in my_lst:
    x = i.split(' ')
    my_lst2 = x[2:-1]
    for i in my_lst2:
        my_lst3.append(i)
date = pd.date_range(start='2/1/2018', end='1/1/2023', freq='MS')
df2 = pd.DataFrame(my_lst3, columns =['Ford_Sales'])
df2 = df2.set_index(date)

my_lst = list()
my_lst2 = list()
my_lst3 = list()
URL = 'https://www.goodcarbadcar.net/volkswagen-group-us-sales-figures/'
content = requests.get(URL)
soup = BeautifulSoup(content.content, 'html.parser')
tags = soup.find_all('tr', id = re.compile(r'table_1812_row_(1[3-7])'))
for tag in tags:
    my_lst.append(tag.get_text().replace("\n", " "))
for i in my_lst:
    x = i.split(' ')
    my_lst2 = x[2:-1]
    for i in my_lst2:
        my_lst3.append(i)
date = pd.date_range(start='2/1/2018', end='1/1/2023', freq='MS')
df3 = pd.DataFrame(my_lst3, columns =['VolksWagen_Sales'])
df3 = df3.set_index(date)

df_car_sales = pd.concat([df1, df2, df3], axis="columns")
#     df_car_sales = df_car_sales.astype(float)

df_gas = pd.read_csv('US_Gas_Price.csv')
df_gas = df_gas.drop(['Date'], axis=1)

date = pd.date_range(start='2/1/2018', end='11/1/2022', freq='MS')
#     df_gas = pd.DataFrame(df_gas, columns =['Gas Price per Month (Dollars per Gallon)'])
df_gas = df_gas.set_index(date)
df_gas.rename(columns = {'U.S. Regular All Formulations Retail Gasoline Prices (Dollars per Gallon)': 'US_gas'}, inplace = True)

df_stockprice_carsales = pd.concat([df_stock_price, df_car_sales], axis="columns")
df_stockprice_carsales = df_stockprice_carsales.apply(lambda x: x.str.replace(',', ''))
df_stockprice_carsales = pd.concat([df_stockprice_carsales, df_gas], axis="columns")
df_stockprice_carsales = df_stockprice_carsales.astype(float)
df = df_stockprice_carsales.drop(['2022-11-01', '2022-12-01', '2023-01-01'])
df = df.drop(['2022-04-01', '2020-05-01', '2022-10-01'])


# # 2.1 Prediction Model of Tesla Stock:

# In[128]:


X = df[['Tesla_Sales', 'US_gas']]
y = df['Tesla_Stock']
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.20, random_state=42)


# In[129]:


# summarize the shape of the training dataset
print(X_train.shape, y_train.shape)


# In[130]:


linear_model = LinearRegression()
model = linear_model.fit(X_train, y_train)


# In[133]:


y_pred=linear_model.predict(X_test)
print("scores:",linear_model.score(X_test,y_test))
print("MAE:", mean_absolute_error(y_test,y_pred))
print("intercept:",linear_model.intercept_)
print("coef_:",linear_model.coef_)


# In[134]:


model.predict(X)


# In[135]:


#Input the actual data of September 2022
new_X = [[37518, 3.7]]
print(model.predict(new_X)) 
#The real number average price is $279


# # 2.2 Prediction model of Ford

# In[65]:


x = df[['Ford_Sales', 'US_gas']]
y = df['Ford_Stock']
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.20, random_state=42)


# In[66]:


linear_model = LinearRegression()
model = linear_model.fit(x_train, y_train)


# In[67]:


y_pred=linear_model.predict(x_test)
print("scores:",linear_model.score(x_test,y_test))
print("MAE:", mean_absolute_error(y_test,y_pred))
print("intercept:",linear_model.intercept_)
print("coef_:",linear_model.coef_)


# In[68]:


model.predict(x)


# In[69]:


#Input the actual data of September 2022
new_X = [[134967, 3.7]]
print(model.predict(new_X))
#The real average price is $14.8


# # 2.3 Prediction Model of VolksWagen

# In[ ]:


x = df[['VolksWagen_Sales', 'US_gas']]
y = df['VolksWagen_Stock']
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.20, random_state=42)


# In[ ]:


linear_model = LinearRegression()
model = linear_model.fit(x_train, y_train)


# In[ ]:


y_pred=linear_model.predict(x_test)
print("scores:",linear_model.score(x_test,y_test))
print("MAE:", mean_absolute_error(y_test,y_pred))
print("intercept:",linear_model.intercept_)
print("coef_:",linear_model.coef_)


# In[ ]:


model.predict(x)


# In[70]:


#Input the actual data of September 2022
new_X = [[50000, 3.7]]
print(model.predict(new_X))
#The real average price is $15.5


# # 3. Linear Regression: Stock Price & Car Sales

# In[97]:


# Tesla Stock Price & Car Sales
print('Tesla_Stock ~ Tesla_Sales')
sns.regplot(x = "Tesla_Sales", y ="Tesla_Stock",  data = df).set(title = "Linear Regression of Tesla Sales and Tesla Stock")

mod = smf.ols("Tesla_Stock ~ Tesla_Sales", data=df)
res = mod.fit()
print(res.summary())


# In[73]:


# Ford Stock Price & Car Sales
print('Ford_Stock ~ Ford_Sales')
mod = ols(formula="Ford_Stock ~ Ford_Sales", data=df)
res = mod.fit()
print(res.summary())
sns.regplot(x = "Ford_Sales", y ="Ford_Stock",  data = df).set(title = "Linear Regression of Ford Sales and Ford Stock")


# In[74]:


# VolksWagen Stock Price & Car Sales
print('VolksWagen_Stock ~ VolksWagen_Sales')
mod = ols(formula="VolksWagen_Stock ~ VolksWagen_Sales", data=df)
res = mod.fit()
print(res.summary())
sns.regplot(x = "VolksWagen_Sales", y ="VolksWagen_Stock",  data = df).set(title = "Linear Regression of VolksWagen Sales and VolksWagen Stock")


# # 4. Linear Regression: Stock Price & Gas Price

# In[94]:


# Tesla Stock Price & Gas Price
print('Tesla_Stock ~ US_gas')
sns.regplot(x = "US_gas", y ="Tesla_Stock",  data = df).set(title = "Linear Regression of Tesla Sales and US gas")

mod = smf.ols("Tesla_Stock ~ US_gas", data=df)
res = mod.fit()
print(res.summary())


# In[95]:


# Ford Stock Price & US gas
print('Ford_Stock ~ US_gas')
mod = ols(formula="Ford_Stock ~ US_gas", data=df)
res = mod.fit()
print(res.summary())
sns.regplot(x = "US_gas", y ="Ford_Stock",  data = df).set(title = "Linear Regression of Ford Sales and US_gas")


# In[96]:


# VolksWagen Stock Price & US gas
print('VolksWagen_Stock ~ US_gas')
mod = ols(formula="VolksWagen_Stock ~ US_gas", data=df)
res = mod.fit()
print(res.summary())
sns.regplot(x = "US_gas", y ="VolksWagen_Stock",  data = df).set(title = "Linear Regression of VolksWagen Sales and US_gas")


# # 5. Visualize The Trend

# In[98]:


# Visualizing The Car Sales of all the Companies
plt.figure(figsize=(6, 3), dpi=100)
df["Tesla_Sales"].plot(label="Tesla_Sales", color='orange')
df['Ford_Sales'].plot(label='Ford_Sales')
df['VolksWagen_Sales'].plot(label='VolksWagen_Sales')

plt.title('Sales Plot of Three Automobile Companies')
plt.xlabel('Year')
plt.legend()

# Visualizing The Open Price of all the stocks
plt.figure(figsize=(6, 3), dpi=100)
df["Tesla_Stock"].plot(label="Tesla_Stock", color='orange')
df['Ford_Stock'].plot(label='Ford_Stock')
df['VolksWagen_Stock'].plot(label='VolksWagen_Stock')
plt.title('Stock Price Plot of Three Automobile Companies')
plt.xlabel('Year')
plt.legend()

# Visualizing The Gas Price
plt.figure(figsize=(6, 3), dpi=100)
df["US_gas"].plot(label="US_gas", color='orange')
plt.title('US Gas Price 2018-2022')
plt.xlabel('Year')
plt.legend()


# In[ ]:




