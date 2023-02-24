#!/usr/bin/env python
# coding: utf-8

# In[20]:

Python setup.py install
pip install beautifulsoup
import sys
from beautifulsoup import BeautifulSoup
import requests
import re
import pandas as pd
import json
import csv

def default_function():
    
    #function_1: Stock Avg Price Monthly: Tesla, Ford, VolksWagen:
    def get_API_to_df():
        response = requests.get('https://api.twelvedata.com/avg?apikey=fc01582d31674d1aa5860ca3e7a5c998&interval=1month&symbol=TSLA&start_date=2018-02-01 00:00:00&format=JSON&end_date=2022-10-02 00:00:00')
        data = json.loads(response.text)
        my_dict2 = data['values']
        df1 = pd.DataFrame.from_dict(my_dict2)
        df1 = df1.loc[::-1].reset_index(drop=True)
        date = pd.date_range(start='2/1/2018', end='10/1/2022', freq='MS')
        df1 = df1.set_index(date)
        df1 = df1.drop('datetime', axis=1)
        df1.rename(columns = {'avg': 'Tesla Avg Stock Price Per Month'}, inplace = True)

        #Frod:
        response = requests.get("https://api.twelvedata.com/avg?apikey=fc01582d31674d1aa5860ca3e7a5c998&interval=1month&start_date=2018-02-01 00:00:00&format=JSON&end_date=2022-10-02 00:00:00&symbol=F")
        data = json.loads(response.text)
        my_dict2 = data['values']
        df2 = pd.DataFrame.from_dict(my_dict2)
        df2 = df2.loc[::-1].reset_index(drop=True)
        date = pd.date_range(start='2/1/2018', end='10/1/2022', freq='MS')
        df2 = df2.set_index(date)
        df2 = df2.drop('datetime', axis=1)
        df2.rename(columns = {'avg': 'Ford Avg Stock Price Per Month'}, inplace = True)

        #VW:
        response = requests.get("https://api.twelvedata.com/avg?apikey=fc01582d31674d1aa5860ca3e7a5c998&interval=1month&start_date=2018-02-01 00:00:00&format=JSON&end_date=2022-10-02 00:00:00&symbol=VWAPY")
        data = json.loads(response.text)
        my_dict2 = data['values']
        df3 = pd.DataFrame.from_dict(my_dict2)
        df3 = df3.loc[::-1].reset_index(drop=True)
        date = pd.date_range(start='2/1/2018', end='10/1/2022', freq='MS')
        df3 = df3.set_index(date)
        df3 = df3.drop('datetime', axis=1)
        df3.rename(columns = {'avg': 'VolksWagen Avg Stock Price Per Month'}, inplace = True)

        df_stock_price = pd.concat([df1, df2, df3], axis="columns")
        df_stock_price.to_csv('Stock_Price.csv', index = True)
        print(df_stock_price.head(10))
    get_API_to_df()

    #function_2: Car Sales Monthly: Tesla, Ford, VolksWagen
    def car_sale():
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
        df1 = pd.DataFrame(my_lst3, columns =['Tesla Car Sales per Month'])
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
        df2 = pd.DataFrame(my_lst3, columns =['Ford Car Sales per Month'])
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
        df3 = pd.DataFrame(my_lst3, columns =['VolksWagen Car Sales per Month'])
        df3 = df3.set_index(date)

        df_car_sales = pd.concat([df1, df2, df3], axis="columns")
        df_car_sales.to_csv('Car_Sales.csv', index = True)
        print(df_car_sales.head(10))
    car_sale()
    return


# In[21]:


def scrape_function():
    #def 1: stock prices
    def get_API_to_df():
        response = requests.get('https://api.twelvedata.com/avg?apikey=fc01582d31674d1aa5860ca3e7a5c998&interval=1month&symbol=TSLA&start_date=2018-02-01 00:00:00&format=JSON&end_date=2022-10-02 00:00:00')
        data = json.loads(response.text)
    #     print(my_dict)
        my_dict2 = data['values'] #list of dic
        #dataframe
        df1 = pd.DataFrame.from_dict(my_dict2)
        df1 = df1.loc[::-1].reset_index(drop=True)
        date = pd.date_range(start='2/1/2018', end='10/1/2022', freq='MS')
        df1 = df1.set_index(date)
        df1 = df1.drop('datetime', axis=1)
        df1.rename(columns = {'avg': 'Tesla Avg Stock Price Per Month'}, inplace = True)

        #Frod:
        response = requests.get("https://api.twelvedata.com/avg?apikey=fc01582d31674d1aa5860ca3e7a5c998&interval=1month&start_date=2018-02-01 00:00:00&format=JSON&end_date=2022-10-02 00:00:00&symbol=F")
        data = json.loads(response.text)
    #     print(my_dict)
        my_dict2 = data['values'] #list of dic
        #dataframe
        df2 = pd.DataFrame.from_dict(my_dict2)
        df2 = df2.loc[::-1].reset_index(drop=True)
        date = pd.date_range(start='2/1/2018', end='10/1/2022', freq='MS')
        df2 = df2.set_index(date)
        df2 = df2.drop('datetime', axis=1)
        df2.rename(columns = {'avg': 'Ford Avg Stock Price Per Month'}, inplace = True)

        #VW:
        response = requests.get("https://api.twelvedata.com/avg?apikey=fc01582d31674d1aa5860ca3e7a5c998&interval=1month&start_date=2018-02-01 00:00:00&format=JSON&end_date=2022-10-02 00:00:00&symbol=VWAPY")
        data = json.loads(response.text)
    #     print(my_dict)
        my_dict2 = data['values'] #list of dic
        #dataframe
        df3 = pd.DataFrame.from_dict(my_dict2)
        df3 = df3.loc[::-1].reset_index(drop=True)
        date = pd.date_range(start='2/1/2018', end='10/1/2022', freq='MS')
        df3 = df3.set_index(date)
        df3 = df3.drop('datetime', axis=1)
        df3.rename(columns = {'avg': 'VolksWagen Avg Stock Price Per Month'}, inplace = True)

        df_stock_price = pd.concat([df1, df2, df3], axis="columns")
#         df_stock_price.to_csv('Stock_Price.csv', index = True)
        print(df_stock_price.head(5))
    get_API_to_df()
    #def 2: car sales
    def car_sale():
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
        df1 = pd.DataFrame(my_lst3, columns =['Tesla Car Sales per Month'])
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
        df2 = pd.DataFrame(my_lst3, columns =['Ford Car Sales per Month'])
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
        df3 = pd.DataFrame(my_lst3, columns =['VolksWagen Car Sales per Month'])
        df3 = df3.set_index(date)

        df_car_sales = pd.concat([df1, df2, df3], axis="columns")
#         df_car_sales.to_csv('Car_Sales.csv', index = True)
        print(df_car_sales.head(5))
    car_sale()
    return


# In[24]:


#what should the path be?

def static_function(path_to_static_data): #path: ./datasets/
    # path_to_static_data = sys.argv[2]
    with open(path_to_static_data+"/Stock_Price.csv", 'r', encoding = 'utf-8-sig') as file:
        data = pd.read_csv(file) 
        print(data)
    with open(path_to_static_data+"/Car_sales.csv", 'r', encoding = 'utf-8-sig') as file:
        data = pd.read_csv(file) 
        print(data)
    with open(path_to_static_data+"/US_Gas_Price.csv", 'r', encoding = 'utf-8-sig') as file:
        data = pd.read_csv(file) 
        print(data)


# In[22]:


if __name__ == '__main__':
    if len(sys.argv) == 1:
        default_function()
    elif sys.argv[1] == '--scrape':
        scrape_function()
    elif sys.argv[1] == '--static':
        path_to_static_data = sys.argv[2]
        static_function(path_to_static_data)

