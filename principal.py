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

#dividir entre treino e teste
from sklearn.model_selection import train_test_split

features_treino,features_teste,classes_treino,classes_teste = train_test_split(features,classes,test_size=0.3,random_state=2)
from sklearn.tree import DecisionTreeClassifier
arvore = DecisionTreeClassifier()

# treina a arvore
arvore.fit(features_treino,classes_treino)

#testa a arvore

resultado = arvore.predict(features_teste)
print("resultado",resultado)

#avalia a precição da arvore é esperada
#from sklearn import metrics
#print(metrics.classification_report(classes_teste,predicao,target_names=nomes_classes))

#resultado = arvore.predict(features_teste)

#avalia a predição da arvore
#from sklearn import metrics

#print(metrics.classification_report(classes_teste,resultado,target_names=['']))



