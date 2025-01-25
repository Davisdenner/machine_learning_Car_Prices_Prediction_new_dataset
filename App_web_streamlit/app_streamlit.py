import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

st.title("Predição do Preço dos Carros")

# Carregar o dataset
@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\Jamylle\Documents\07-Regressao-linear-preço-de-carros\dataset\CarPrice_Assignment.csv")
    # Renomeando a coluna de marca de carros
    df['car_brands'] = df['CarName'].str.split(' ').str[0]
    df.insert(1, 'car_brands', df.pop('car_brands'))
    # Apagando as colunas desnecessárias para a análise
    df.drop(['CarName', 'car_ID', 'symboling'], axis=1, inplace=True)
    
    # Corrigir nomes de marcas de carros
    def fix_company_name(old_name, new_name):
        df['car_brands'].replace(old_name, new_name, inplace=True)
    
    fix_company_name('maxda', 'mazda')
    fix_company_name('nissan', 'Nissan')
    fix_company_name('vw', 'volkswagen')
    fix_company_name('toyouta', 'toyota')
    fix_company_name('porcshce', 'porsche')
    fix_company_name('vokswagen', 'volkswagen')

    # Convertendo variáveis categóricas para numéricas
    df['fueltype'] = df['fueltype'].replace({'gas': 1, 'diesel': 0}).astype(int)
    df['doornumber'] = df['doornumber'].replace({'two': 2, 'four': 4}).astype(int)
    df['aspiration'] = df['aspiration'].replace({'std': 1, 'turbo': 0}).astype(int)
    df['drivewheel'] = df['drivewheel'].replace({'fwd': 1, 'rwd': 2, '4wd': 3}).astype(int)
    df['enginelocation'] = df['enginelocation'].replace({'front': 1, 'rear': 0}).astype(int)
    df['cylindernumber'] = df['cylindernumber'].replace({'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'eight': 8, 'twelve': 12}).astype(int)
    
    # Criando variáveis dummies para colunas categóricas
    enginetype_dummies = pd.get_dummies(df['enginetype'], drop_first=True, prefix='enginetype')
    df = pd.concat([df, enginetype_dummies], axis=1)
    df.drop('enginetype', axis=1, inplace=True)

    carbody_dummies = pd.get_dummies(df['carbody'], drop_first=True, prefix='carbody')
    df = pd.concat([df, carbody_dummies], axis=1)
    df.drop('carbody', axis=1, inplace=True)

    fuelsystem_dummies = pd.get_dummies(df['fuelsystem'], drop_first=True, prefix='fuelsystem')
    df = pd.concat([df, fuelsystem_dummies], axis=1)
    df.drop('fuelsystem', axis=1, inplace=True)
    
    return df

# Carregar dados
df = load_data()

# Dividir os dados em variáveis independentes e dependentes
y = df["price"]
x = df.drop(["price"], axis=1)

# Dividir os dados em treino e teste
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

# Criando um pré-processador para lidar com variáveis categóricas e numéricas
preprocessor = ColumnTransformer(
    transformers=[
        ('num', 'passthrough', x.select_dtypes(include=['int64', 'float64']).columns),
        ('cat', OneHotEncoder(sparse_output=False, handle_unknown='ignore'), ['car_brands'])
    ])

# Criação do pipeline com pré-processamento e modelo
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

# Ajuste do modelo
model_pipeline.fit(x_train, y_train)

# Função de predição
def predict_price(input_data):
    input_df = pd.DataFrame([input_data], columns=x.columns)
    return model_pipeline.predict(input_df)[0]

# Interface do Streamlit
st.sidebar.header("Insira as Características do Carro")

# Coletando os dados de entrada
input_data = {col: st.sidebar.number_input(col, float(df[col].min()), float(df[col].max()), float(df[col].mean())) for col in x.columns if col != 'car_brands'}
input_data['car_brands'] = st.sidebar.selectbox("Marca do Carro", df['car_brands'].unique())

# Exibir a previsão
if st.sidebar.button("Prever Preço"):
    st.write(f"### Preço Estimado: ${predict_price(input_data):.2f}")
    

# Gráfico de contagem das marcas de carros
st.subheader("Distribuição de vendsas das Marcas de Carros")
fig, ax = plt.subplots()
df['car_brands'].value_counts().plot(kind='bar', color='blue', edgecolor='yellow', ax=ax)
st.pyplot(fig)


