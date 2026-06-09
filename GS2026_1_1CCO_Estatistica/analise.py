# GS2026.1 - Analise Estatistica - Missoes Espaciais 1957-2020
# Modelagem Linear para Aprendizado de Maquina
# Equipe AstroTeam (Dupla)
# Joao Vitor Belchior Domingos Leite - RM: 572478
# Gabriel Pedro de Souza - RM: 571995

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cria a pasta dos graficos
os.makedirs("graficos", exist_ok=True)


# ============================================================
# 1. LEITURA DA BASE DE DADOS
# ============================================================
df = pd.read_csv("dados.csv")
print("Total de missoes na base:", len(df))

# Extrai o ano direto da string da data (pega os 4 digitos) e converte o custo em numero
df["Ano"] = df["Datum"].astype(str).str.extract(r"(\d{4})")[0].astype("Int64")
df["Custo"] = pd.to_numeric(df[" Rocket"].str.replace(",", "").str.strip(), errors="coerce")

# Variaveis que vamos analisar
ano = df["Ano"].dropna()
custo = df["Custo"].dropna()


# ============================================================
# 2. TABELA DE FREQUENCIA - VARIAVEL DISCRETA (Ano)
# ============================================================
print("\n--- Tabela de Frequencia: Ano de Lancamento ---")

fi = ano.value_counts().sort_index()
fac = fi.cumsum()
total = fi.sum()

tabela_ano = pd.DataFrame({
    "Ano": fi.index,
    "Fi": fi.values,
    "Fr (%)": np.round(fi.values / total * 100, 2),
    "Fac": fac.values,
    "Frac (%)": np.round(fac.values / total * 100, 2),
})
print(tabela_ano.to_string(index=False))


# ============================================================
# 3. TABELA DE FREQUENCIA - VARIAVEL CONTINUA (Custo)
# ============================================================
print("\n--- Tabela de Frequencia: Custo do Foguete (5 classes) ---")

# Divide o custo em 5 faixas (classes) de tamanho igual
faixas = pd.cut(custo, bins=5)
fi2 = faixas.value_counts().sort_index()
fac2 = fi2.cumsum()
total2 = fi2.sum()

tabela_custo = pd.DataFrame({
    "Classe": fi2.index.astype(str),
    "Fi": fi2.values,
    "Fr (%)": np.round(fi2.values / total2 * 100, 2),
    "Fac": fac2.values,
    "Frac (%)": np.round(fac2.values / total2 * 100, 2),
})
print(tabela_custo.to_string(index=False))


# ============================================================
# 4. GRAFICO 1 - LANCAMENTOS POR DECADA (variavel discreta)
# ============================================================
decada = (ano // 10) * 10
contagem = decada.value_counts().sort_index()

plt.figure(figsize=(10, 6))
plt.bar(contagem.index.astype(int).astype(str), contagem.values,
        color="steelblue", edgecolor="black")
plt.title("Lancamentos Espaciais por Decada (1957-2020)")
plt.xlabel("Decada")
plt.ylabel("Numero de Lancamentos")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.savefig("graficos/grafico_lancamentos_decada.png", dpi=150)
plt.close()
print("\nGrafico 1 salvo: graficos/grafico_lancamentos_decada.png")


# ============================================================
# 5. GRAFICO 2 - HISTOGRAMA DO CUSTO (variavel continua)
# ============================================================
plt.figure(figsize=(10, 6))
plt.hist(custo, bins=20, color="steelblue", edgecolor="black")
plt.axvline(custo.mean(), color="red", linestyle="--",
            label=f"Media: {custo.mean():.2f}M USD")
plt.axvline(custo.median(), color="green", linestyle="--",
            label=f"Mediana: {custo.median():.2f}M USD")
plt.title("Distribuicao do Custo dos Foguetes (Milhoes USD)")
plt.xlabel("Custo do foguete (milhoes USD)")
plt.ylabel("Frequencia (escala log)")
plt.yscale("log")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.savefig("graficos/grafico_custo_foguetes.png", dpi=150)
plt.close()
print("Grafico 2 salvo: graficos/grafico_custo_foguetes.png")


# ============================================================
# 6. ANALISE UNIVARIADA - ANO DE LANCAMENTO
# ============================================================
print("\n--- Analise Univariada: Ano de Lancamento ---")
print("Media         :", round(ano.mean(), 2))
print("Mediana       :", ano.median())
print("Moda          :", ano.mode()[0])
print("Maximo        :", ano.max())
print("Minimo        :", ano.min())
print("Amplitude     :", ano.max() - ano.min())
print("Variancia     :", round(ano.var(), 2))
print("Desvio padrao :", round(ano.std(), 2))
print("Coef. variacao:", round(ano.std() / ano.mean() * 100, 2), "%")
print("Q1            :", ano.quantile(0.25))
print("Q2 (mediana)  :", ano.quantile(0.50))
print("Q3            :", ano.quantile(0.75))


# ============================================================
# 7. ANALISE UNIVARIADA - CUSTO DO FOGUETE
# ============================================================
print("\n--- Analise Univariada: Custo do Foguete (milhoes USD) ---")
print("Media         :", round(custo.mean(), 2))
print("Mediana       :", custo.median())
print("Moda          :", custo.mode()[0])
print("Maximo        :", custo.max())
print("Minimo        :", custo.min())
print("Amplitude     :", round(custo.max() - custo.min(), 2))
print("Variancia     :", round(custo.var(), 2))
print("Desvio padrao :", round(custo.std(), 2))
print("Coef. variacao:", round(custo.std() / custo.mean() * 100, 2), "%")
print("Q1            :", custo.quantile(0.25))
print("Q2 (mediana)  :", custo.quantile(0.50))
print("Q3            :", custo.quantile(0.75))

print("\nFim da analise.")
