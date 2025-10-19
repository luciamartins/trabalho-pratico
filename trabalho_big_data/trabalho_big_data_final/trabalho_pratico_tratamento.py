# TRABALHO PRÁTICO - TRATAMENTO DE DADOS PICO WEB
# DGT2823 - Tecnologias para desenvolvimento de soluções de big data

print(" TRABALHO PRÁTICO - TRATAMENTO DE DADOS PICO WEB")
print("=" * 55)

import pandas as pd
import numpy as np

# Leitura do CSV
dados_originais = pd.read_csv('pico_web.csv', sep=';', engine='python', encoding='utf-8')

print("✅ Dados importados com sucesso!")
print(f"📊 Dimensões iniciais: {dados_originais.shape}")

# Verificação inicial
print("\n🔍 Primeiras 5 linhas:")
print(dados_originais.head())

# Criar cópia para tratamento
dados_tratados = dados_originais.copy()

# Substituir NaN em Calories por 0
dados_tratados['Calories'].fillna(0, inplace=True)

# Substituir NaN em Date por '1900/01/01' (depois corrigiremos)
dados_tratados['Date'].fillna('1900/01/01', inplace=True)

# Tentar converter para datetime (vai falhar)
try:
    dados_tratados['Date'] = pd.to_datetime(dados_tratados['Date'])
except Exception as e:
    print(f"❌ Erro na primeira conversão: {e}")

# Corrigir '1900/01/01' para NaN
dados_tratados['Date'] = dados_tratados['Date'].replace('1900/01/01', np.nan)

# Corrigir '20201226' para datetime
dados_tratados['Date'] = dados_tratados['Date'].replace('20201226', pd.to_datetime('20201226', format='%Y%m%d'))

# Converter toda a coluna para datetime
dados_tratados['Date'] = pd.to_datetime(dados_tratados['Date'])

# Remover registros com valores nulos
dados_tratados = dados_tratados.dropna()

print(f"\n✅ Dataset final: {dados_tratados.shape}")
print("\n📅 Tipos de dados finais:")
print(dados_tratados.dtypes)

print("\n🎉 TRABALHO CONCLUÍDO!")
