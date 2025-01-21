# -*- coding: utf-8 -*-
"""Prices_Prediction_incompleto

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fJNk4x4vKLp16yCH-p7cY8BrPUfc5ZtS
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df=pd.read_csv('/content/CarPrice_Assignment.csv')

df.head()

#Renomeando a coluna de marca de carros
df['car_brands']=df['CarName'].str.split(' ').str[0]
df.insert(1,'car_brands',df.pop('car_brands'))
df.head()

#Apagando as colunas desnecessárias para a análise
df.drop(['CarName', 'car_ID', 'symboling'], axis=1, inplace=True)

df.head()

df.info()

df['car_brands'].unique()

#Renomeando nome das marcas corretamente.

def fix_company_name(old_name, new_name):
    df['car_brands'].replace(old_name, new_name, inplace=True)

fix_company_name('maxda' , 'mazda')
fix_company_name('nissan' , 'Nissan')
fix_company_name('vw' , 'volkswagen')
fix_company_name('toyouta' , 'toyota')
fix_company_name('porcshce' , 'porsche')
fix_company_name('vokswagen' , 'volkswagen')

df['car_brands'].unique()

df['price'].describe()

#Análise das vendas
plt.title('company_sales')
df['car_brands'].value_counts().plot(kind='bar',color='blue',edgecolor='yellow')

plt.title('fueltype')
df['fueltype'].value_counts().plot(kind='pie',autopct='%1.1f%%',colors=['red','y'],explode=[0,0.3])

df.hist(figsize=(14,14))

df.head()

df.columns

df['fueltype'].unique()

df['enginetype'].unique()

df['cylindernumber'].unique()

df['drivewheel'].unique()

df['fuelsystem'].unique()

df['carbody'].unique()

df.head()

