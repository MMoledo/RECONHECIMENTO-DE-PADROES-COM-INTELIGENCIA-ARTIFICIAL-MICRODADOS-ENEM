from pyspark.sql.functions import col, create_map, lit
from itertools import chain

q001_dict = {
    'A': 1,  # Nunca estudou.
    'B': 2,  # Não completou a 4ª série/5º ano do Ensino Fundamental.
    'C': 3,  # Completou a 4ª série/5º ano, mas não completou a 8ª série/9º ano do Ensino Fundamental.
    'D': 4,  # Completou a 8ª série/9º ano do Ensino Fundamental, mas não completou o Ensino Médio.
    'E': 5,  # Completou o Ensino Médio, mas não completou a Faculdade.
    'F': 6,  # Completou a Faculdade, mas não completou a Pós-graduação.
    'G': 7,  # Completou a Pós-graduação.
    'H': 8  # Não sei.
}
q002_dict = {
    'A': 1,  # Nunca estudou.
    'B': 2,  # Não completou a 4ª série/5º ano do Ensino Fundamental.
    'C': 3,  # Completou a 4ª série/5º ano, mas não completou a 8ª série/9º ano do Ensino Fundamental.
    'D': 4,  # Completou a 8ª série/9º ano do Ensino Fundamental, mas não completou o Ensino Médio.
    'E': 5,  # Completou o Ensino Médio, mas não completou a Faculdade.
    'F': 6,  # Completou a Faculdade, mas não completou a Pós-graduação.
    'G': 7,  # Completou a Pós-graduação.
    'H': 8  # Não sei.
}
q003_dict = {
    'A': 1,  # Grupo 1: Lavrador, agricultor sem empregados, bóia fria, criador de animais etc.
    'B': 2,  # Grupo 2: Diarista, empregado doméstico, cuidador de idosos, babá, cozinheiro etc.
    'C': 3,  # Grupo 3: Padeiro, cozinheiro industrial ou em restaurantes, sapateiro, costureiro etc.
    'D': 4,  # Grupo 4: Professor, técnico, policial, militar de baixa patente, corretor de imóveis etc.
    'E': 5,  # Grupo 5: Médico, engenheiro, dentista, psicólogo, economista, advogado etc.
    'F': 6   # Não sei.
}
q004_dict = {
    'A': 1,  # Grupo 1: Lavradora, agricultora sem empregados, bóia fria, criadora de animais etc.
    'B': 2,  # Grupo 2: Diarista, empregada doméstica, cuidadora de idosos, babá, cozinheira etc.
    'C': 3,  # Grupo 3: Padeira, cozinheira industrial ou em restaurantes, sapateira, costureira etc.
    'D': 4,  # Grupo 4: Professora, técnica, policial, militar de baixa patente, corretora de imóveis etc.
    'E': 5,  # Grupo 5: Médica, engenheira, dentista, psicóloga, economista, advogada etc.
    'F': 6   # Não sei.
}
'''
q005_dict = {
    1: 1,   # 1, pois moro sozinho(a).
    2: 2,   # 2
    3: 3,   # 3
    4: 4,   # 4
    5: 4,   # 5
    6: 4,   # 6
    7: 4,   # 7
    8: 4,   # 8
    9: 4,   # 9
    10: 4, # 10
    11: 4, # 11
    12: 4, # 12
    13: 4, # 13
    14: 4, # 14
    15: 4, # 15
    16: 4, # 16
    17: 4, # 17
    18: 4, # 18
    19: 4, # 19
    20: 4  # 20
}
'''

q006_dict = {
    'A': 1,  # Nenhuma Renda
    'B': 2,  # Até R$ 1.212,00
    'C': 3,  # De R$ 1.212,01 até R$ 1.818,00.
    'D': 4,  # De R$ 1.818,01 até R$ 2.424,00.
    'E': 5,  # De R$ 2.424,01 até R$ 3.030,00.
    'F': 6,  # De R$ 3.030,01 até R$ 3.636,00.
    'G': 7,  # De R$ 3.636,01 até R$ 4.848,00.
    'H': 8,  # De R$ 4.848,01 até R$ 6.060,00.
    'I': 9,  # De R$ 6.060,01 até R$ 7.272,00.
    'J': 10,  # De R$ 7.272,01 até R$ 8.484,00.
    'K': 11,  # De R$ 8.484,01 até R$ 9.696,00.
    'L': 12,  # De R$ 9.696,01 até R$ 10.908,00.
    'M': 13,  # De R$ 10.908,01 até R$ 12.120,00.
    'N': 14,  # De R$ 12.120,01 até R$ 14.544,00.
    'O': 15,  # De R$ 14.544,01 até R$ 18.180,00.
    'P': 16,  # De R$ 18.180,01 até R$ 24.240,00.
    'Q': 17   # Acima de R$ 24.240,00.
}

q022_dict = {
    'A': 1,  # Não.
    'B': 2,  # Sim, um.
    'C': 3,  # Sim, dois.
    'D': 3,  # Sim, três.
    'E': 3   # Sim, quatro ou mais.
}

q024_dict = {
    'A': 1,  # Não.
    'B': 2,  # Sim, um.
    'C': 3,  # Sim, dois.
    'D': 3,  # Sim, três.
    'E': 3   # Sim, quatro ou mais.
}
q025_dict = {
    'A': 0,  # Não.
    'B': 1   # Sim.
}

