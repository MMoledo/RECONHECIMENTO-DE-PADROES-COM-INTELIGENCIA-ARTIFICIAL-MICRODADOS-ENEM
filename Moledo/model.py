import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import dic  # Supondo que 'dic' é um módulo que contém mapeamentos de colunas

# Carregamento dos dados
df = pd.read_csv('limpo.csv', sep=';', encoding='latin1')
colunas = [
    "TP_FAIXA_ETARIA", "TP_SEXO", "TP_ESTADO_CIVIL", "TP_COR_RACA",
    "TP_NACIONALIDADE", "TP_ST_CONCLUSAO", "TP_ANO_CONCLUIU", "TP_ESCOLA", "IN_TREINEIRO", "TP_LINGUA",
    "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "NU_NOTA_REDACAO",
    "Q001", "Q002", "Q003", "Q004", "Q006", "Q024"
]
df = df[colunas].dropna()
df = df[(df['Q002'] != 'H') & (df['Q001'] != 'H')]

# Mapeamento de colunas
for coluna in dic.colunas_dic:
    nome_dict = coluna.lower() + '_dict'
    if hasattr(dic, nome_dict):
        mapeamento = getattr(dic, nome_dict)
        df[coluna] = df[coluna].replace(mapeamento)

mapeamento_sexo = {'M': 1, 'F': 0}
df['TP_SEXO'] = df['TP_SEXO'].replace(mapeamento_sexo)

# Cálculo da média e classificação
df['MEDIAS'] = df[['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']].mean(axis=1)
limite_baixo = df['MEDIAS'].quantile(0.33)
limite_alto = df['MEDIAS'].quantile(0.66)
df['CLASSE_MEDIAS'] = pd.cut(df['MEDIAS'], bins=[0, limite_baixo, limite_alto, float('inf')], labels=['baixo', 'médio', 'alto'])
df = df.drop(columns=['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO', 'MEDIAS'])
print(df.head())
# Preparação dos dados para modelagem
X = df.drop('CLASSE_MEDIAS', axis=1)
y = df['CLASSE_MEDIAS']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelagem usando Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Avaliação do modelo
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia do modelo: {accuracy:.2f}')
