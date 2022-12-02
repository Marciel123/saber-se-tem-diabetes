import streamlit as st
import pandas as pd #manipulacao 
from sklearn.model_selection import train_test_split
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
individuo = []
diagnostico = ['Não diabético','Diabético']
f1 = st.number_input('Digite o número de gravidez do indivíduo')
f2 = st.number_input('Digite o número de gravidez do indivíduo')
f3 = st.number_input('Digite o número de glucose (0-199)')
f4 = st.number_input('Digite a pressão sanguínea (0-122)')
f5 = st.number_input('Digite a espessura da pele (0-99)')
f6 = st.number_input('Digite o valor da insulina (0-846)')
f7 = st.number_input('Digite o IMC (0-67.1)')
f8 = st.number_input('Digite o pedigree de 0.07 a 2.2')
f8 = st.number_input('Digite a idade (21-81)')

#Diabetes Pedigree Function ou Função de linhagem de diabetes: indica a função que pontua a probabilidade de diabetes com base na história familiar

individuo.append(DiabetesPedigreeFunction)

individuo.append(Age)

resposta = arvore.predict([individuo])
print(diagnostico[int(resposta)])


