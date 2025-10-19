# TRABALHO PRÁTICO - DGT2823 - BIG DATA
# Aluno: [LUCIA MARIA DE LIMA MARTINS]
# Matrícula: [202309761581]

print("TRABALHO PRÁTICO - TODAS MICROATIVIDADES")
print("=" * 50)

# ========== MICROATIVIDADE 1 ==========
print("\n MICROATIVIDADE 1: Ler arquivo CSV")
print("=" * 40)

import pandas as pd

# Ler arquivo CSV com todos os parâmetros solicitados
dados_dataframe = pd.read_csv(
    'pico_web.csv',
    sep=';',           # Separador de colunas
    engine='python',   # Engine com valor 'python'
    encoding='utf-8'  # Encoding
)

print("Arquivo CSV lido com sucesso!")
print("Dados carregados:")
print(dados_dataframe)
print(f"Dimensões: {dados_dataframe.shape}")

# ========== MICROATIVIDADE 2 ==========
print("\n MICROATIVIDADE 2: Criar subconjunto de dados")
print("=" * 45)

# Criar subconjunto com 3 colunas
subconjunto_dados = dados_dataframe[['Duration', 'Pulse', 'Calories']]

print("Subconjunto criado com 3 colunas")
print("Dados do subconjunto:")
print(subconjunto_dados)
print(f"Dimensões do subconjunto: {subconjunto_dados.shape}")

# ========== MICROATIVIDADE 3 ==========
print("\n MICROATIVIDADE 3: Configurar número máximo de linhas")
print("=" * 50)

# Configurar visualização para 8 linhas
pd.set_option('display.max_rows', 8)
print("Configurado display.max_rows = 8")

print("Dataset com limite de linhas:")
print(dados_dataframe)

# ========== MICROATIVIDADE 4 ==========
print("\n MICROATIVIDADE 4: Exibir primeiras e últimas linhas")
print("=" * 50)

print("Primeiras 5 linhas:")
print(dados_dataframe.head())

print("\nÚltimas 5 linhas:")
print(dados_dataframe.tail())

print("\nPrimeiras 3 linhas:")
print(dados_dataframe.head(3))

print("\nÚltimas 3 linhas:")
print(dados_dataframe.tail(3))

# ========== MICROATIVIDADE 5 ==========
print("\n MICROATIVIDADE 5: Exibir informações gerais")
print("=" * 50)

print("Informações do dataset (.info()):")
print(dados_dataframe.info())

print("\nEstatísticas descritivas (.describe()):")
print(dados_dataframe.describe())

print("\n Dimensões do dataset:")
print(f"Linhas: {dados_dataframe.shape[0]}, Colunas: {dados_dataframe.shape[1]}")

print("\nTipos de dados:")
print(dados_dataframe.dtypes)

print("\n" + "=" * 50)
print("TODAS MICROATIVIDADES CONCLUÍDAS COM SUCESSO! 🎉")
print("=" * 50)
