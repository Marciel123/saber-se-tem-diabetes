import streamlit as st
import pandas as pd #manipulacao 


###################importando os dados do csv ########################
dados = pd.read_csv("diabetes.csv")

#coleta os nomes das colunas
nomes_colunas = dados.columns.to_list()
tamanho = len(nomes_colunas)
nomes_colunas = nomes_colunas[:tamanho-1]
features = dados[nomes_colunas]
classes = dados['Outcome']
features.shape,classes.shape
st.write(nomes_colunas)
#dividir entre treino e teste
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics



