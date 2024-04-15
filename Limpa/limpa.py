import pandas as pd


collums = [
    "TP_FAIXA_ETARIA", "TP_SEXO", "TP_ESTADO_CIVIL", "TP_COR_RACA",
    "TP_NACIONALIDADE", "TP_ST_CONCLUSAO", "TP_ANO_CONCLUIU", "TP_ESCOLA",
    "TP_ENSINO", "IN_TREINEIRO", "CO_UF_PROVA", "SG_UF_PROVA",
    "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT",
    "NU_NOTA_REDACAO","TP_LINGUA", "Q001", "Q002", "Q003", "Q004", "Q005", "Q006",
    "Q007", "Q008", "Q009", "Q010", "Q011", "Q012", "Q013", "Q014",
    "Q015", "Q016", "Q017", "Q018", "Q019", "Q020", "Q021", "Q022",
    "Q023", "Q024", "Q025"]


# Carregando o dataframe
df = pd.read_csv('MICRODADOS_ENEM_2022.csv', encoding='latin1', sep=';')

# Eliminando linhas onde todas as colunas específicas têm o valor 0
colunas_presenca = ['TP_PRESENCA_CN', 'TP_PRESENCA_CH', 'TP_PRESENCA_LC', 'TP_PRESENCA_MT']
df = df[(df[colunas_presenca] == 1).any(axis=1)]


new_df = df[collums]
new_df.to_csv('limpo.csv', index=False, sep=';')