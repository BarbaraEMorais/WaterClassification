import pandas as pd
from WaterClassifier.classificacao import classificaDados

#importando database utilizada

dataBase= "water_dataX.csv"
dadosPreProcessados = pd.read_csv(dataBase, encoding='unicode_escape')
#print(dadosPreProcessados)


#convertendo objetos para float para análise
dadosPreProcessados.rename(columns={'D.O. (mg/l)': 'DO'}, inplace = True)
dadosPreProcessados.rename(columns={'CONDUCTIVITY':'CONDUCTIVITY'}, inplace = True)
dadosPreProcessados.rename(columns={'B.O.D. (mg/l)': 'BOD'}, inplace = True)
dadosPreProcessados.rename(columns={'NITRATENAN N+ NITRITENANN (mg/l)': 'NITeNIT'}, inplace = True)
dadosPreProcessados.rename(columns={'FECAL COLIFORM (MPN/100ml)': 'FeCo'}, inplace = True)
dadosPreProcessados.rename(columns={'TOTAL COLIFORM (MPN/100ml)Mean': 'ToCol'}, inplace = True)
dadosPreProcessados = dadosPreProcessados.astype({'DO':'float','CONDUCTIVITY':'float', 'BOD': 'float', 'NITeNIT': 'float', 'FeCo': 'float', 'ToCol': 'float', 'PH': 'float', 'Temp': 'float'})

#passando para outra planilha para edição
dadosPreProcessados.to_csv('dadosClassificados.csv')
teste = 'dadosClassificados.csv'
dados = pd.read_csv(teste)
dados = dados.dropna() 

###CÁLCULO DE PARÂMETROS PARA FAZER CLASSIFICAÇÃO SEGUNDO ARTIGO

#valores tabelados e calculados
#Variáveis Globais

soma = 0
N = 7
Si = [10,8.5,1000,45,5,100,1000]
Videal = [14.6,7.0,0,0,0,0,0]
Wi = [0,0,0,0,0,0,0]
array_wqi = []
classe_qualidade = []
wqi_column = []

classes_qualidade_agua = ['Clean', 'Unclean', 'Polluted', 'Highly Polluted']
classes_metodos = ['KNN', 'SVM', 'MLP', 'ÁRVORE DE DECISÃO', 'NAIVE BAYES']


DO = dados['DO'].copy()
PH = dados['PH'].copy()
CONDUCTIVITY = dados['CONDUCTIVITY'].copy()
BOD = dados['BOD'].copy()
NITeNIT = dados['NITeNIT'].copy()
FeCo = dados['FeCo'].copy()
ToCol = dados['ToCol'].copy()

#obtendo K
for valor in range(len(Si)):
  soma += Si[valor]
K = 1/soma

#obtendo Wi
for valor in range (len(Si)):
  Wi[valor] = K/Si[valor]


#FUNÇÕES UTILIZADAS

def valorQi(Vi):

  Qi = [0,0,0,0,0,0,0]

  for item in range(len(Si)):
    #Qi[item] = 100 * ((Vi[item]-Videal[item])/(Si[item]-Videal[item]))
    Qi[item] = (Vi[item]-Videal[item])/(Si[item]-Videal[item])

  return Qi

def valorWQI(Qi):

  soma1 = 0
  soma2 = 0

  for i in range(N):
    soma1 += Qi[i] * Wi[i]
    soma2 += Wi[i]

  WQI = soma1 / soma2
  array_wqi.append(WQI)

  if WQI>=0 and WQI<=0.25:

    return "Clean"

  elif WQI>0.25 and WQI<=0.50:

    return "Unclean"

  elif WQI>0.50 and WQI<=0.75:

    return "Polluted"

  else:
    return "Highly Polluted"

#REALIZA TODAS AS OPERAÇÕES PARA CLASSIFICAÇÃO

for index, row in dados.iterrows():
  input = [row["DO"], row["PH"], row["CONDUCTIVITY"], row["BOD"], row["NITeNIT"], row["FeCo"], row["ToCol"]]
  #QI
  valQI = valorQi(input)

  #WQI
  valWQI = valorWQI(valQI)

  soma1 = 0
  soma2 = 0

  for i in range(N):
    soma1 += valQI[i] * Wi[i]
    soma2 += Wi[i]

  WQI = soma1 / soma2

  wqi_column.append(valWQI)
  classe_qualidade.append(classes_qualidade_agua.index(valWQI))

dados['WQI'] = wqi_column
dados['classe'] = classe_qualidade
#dados['classe'].value_counts()

####### INICIO DO PROCESSO DE CLASSIFICACAO: DADOS E TARGETS

classificaDados(dados, classes_metodos,classes_qualidade_agua)