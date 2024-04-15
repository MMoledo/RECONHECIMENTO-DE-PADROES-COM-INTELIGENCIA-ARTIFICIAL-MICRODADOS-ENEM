import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import dic  # Supondo que 'dic' é um módulo que contém mapeamentos de colunas

# Carregamento dos dados
df = pd.read_csv('limpo.csv', sep=',', encoding='latin1')
colunas = [
    "TP_FAIXA_ETARIA", "TP_SEXO", "TP_COR_RACA",
     "TP_ESCOLA", "TP_DEPENDENCIA_ADM_ESC",
    "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT",
    "NU_NOTA_REDACAO", "Q006"]
df = df[colunas].dropna()

mapeamento_sexo = {'M': 1, 'F': 0}

# Suponhamos que 'df_microdados' seja seu DataFrame
# Aplicando o mapeamento à coluna 'TP_SEXO'
df['TP_SEXO'] = df['TP_SEXO'].replace(mapeamento_sexo)

# Mapeamento de colunas
for coluna in dic.colunas_dic:
    nome_dict = coluna.lower() + '_dict'
    if hasattr(dic, nome_dict):
        mapeamento = getattr(dic, nome_dict)
        df[coluna] = df[coluna].replace(mapeamento)
        
        

# Cálculo da média e classificação
df['MEDIAS'] = df[['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']].mean(axis=1)
print(df['MEDIAS'].head())
df['CLASSE_MEDIAS'] = pd.cut(df['MEDIAS'], bins=[0, 500,float('inf')], labels=['baixo','alto'])
df = df.drop(columns=['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO', 'MEDIAS'])
print(df.head())
df = df.dropna()
print(df['CLASSE_MEDIAS'].value_counts())
# Preparação dos dados para modelagem
X = df.drop('CLASSE_MEDIAS', axis=1)
y = df['CLASSE_MEDIAS']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Avaliação do
# Modelagem usando Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Avaliação do
model.fit(X_train, y_train)

# Avaliação do modelo
y_pred = model.predict(X_test)

# Avaliação do
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia do modelo: {accuracy:.2f}')

y_pred = model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)

# Visualização da matriz de confusão
fig, ax = plt.subplots(figsize=(8, 8))  # Ajuste o tamanho conforme necessário
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
disp.plot(cmap=plt.cm.Blues, ax=ax)
plt.title('Matriz de Confusão')
plt.xlabel('Previsões')
plt.ylabel('Verdadeiros')
plt.show()
