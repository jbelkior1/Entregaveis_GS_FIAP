# GS2026.1 - Analise Estatistica - Missoes Espaciais 1957-2020
# Equipe AstroTeam
# Joao Vitor Belchior - RM: 572478
# Gabriel Pedro de Souza - RM: 571995

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configuracao
PASTA = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_DADOS = os.path.join(PASTA, "dados.csv")
PASTA_GRAFICOS = os.path.join(PASTA, "graficos")
os.makedirs(PASTA_GRAFICOS, exist_ok=True)


def carregar_dados():
    """Le o CSV e prepara as variaveis para a analise."""
    df = pd.read_csv(ARQUIVO_DADOS)

    # Variavel discreta: Ano do lancamento (extraido da data)
    df["Ano"] = pd.to_datetime(df["Datum"], errors="coerce", utc=True).dt.year

    # Variavel continua: Custo do foguete em milhoes de USD
    df["CustoFoguete"] = (
        df[" Rocket"].astype(str).str.replace(",", "").str.strip()
    )
    df["CustoFoguete"] = pd.to_numeric(df["CustoFoguete"], errors="coerce")

    return df


def tabela_frequencia_discreta(serie, titulo):
    """Tabela de Distribuicao de Frequencia para variavel discreta."""
    print("=" * 70)
    print(f"TABELA DE DISTRIBUICAO DE FREQUENCIA - {titulo} (discreta)")
    print("=" * 70)

    serie = serie.dropna().astype(int)
    total = len(serie)
    contagem = serie.value_counts().sort_index()

    tabela = pd.DataFrame({
        "Valor": contagem.index,
        "Fi": contagem.values,
        "Fr (%)": (contagem.values / total * 100).round(2),
        "Fac": np.cumsum(contagem.values),
        "Frac (%)": np.cumsum(contagem.values / total * 100).round(2),
    })
    print(tabela.to_string(index=False))
    print(f"\nTotal de observacoes: {total}")
    print()
    return tabela


def tabela_frequencia_continua(serie, titulo, n_classes=None):
    """Tabela de Distribuicao de Frequencia para variavel continua (Sturges)."""
    print("=" * 70)
    print(f"TABELA DE DISTRIBUICAO DE FREQUENCIA - {titulo} (continua)")
    print("=" * 70)

    serie = serie.dropna()
    total = len(serie)

    if n_classes is None:
        n_classes = 5

    minimo, maximo = serie.min(), serie.max()
    amplitude = maximo - minimo
    h = amplitude / n_classes

    limites = [minimo + i * h for i in range(n_classes + 1)]
    fi, fr, fac, frac, pontos_medios, intervalos = [], [], [], [], [], []
    acumulado_fi = 0
    acumulado_fr = 0.0
    for i in range(n_classes):
        li, ls = limites[i], limites[i + 1]
        if i == n_classes - 1:
            qtd = ((serie >= li) & (serie <= ls)).sum()
        else:
            qtd = ((serie >= li) & (serie < ls)).sum()
        fi.append(qtd)
        fr_pct = qtd / total * 100
        fr.append(round(fr_pct, 2))
        acumulado_fi += qtd
        acumulado_fr += fr_pct
        fac.append(acumulado_fi)
        frac.append(round(acumulado_fr, 2))
        pontos_medios.append(round((li + ls) / 2, 2))
        intervalos.append(f"[{li:.2f} - {ls:.2f}{']' if i == n_classes - 1 else ')'}")

    tabela = pd.DataFrame({
        "Classe": [f"C{i+1}" for i in range(n_classes)],
        "Intervalo": intervalos,
        "Ponto medio": pontos_medios,
        "Fi": fi,
        "Fr (%)": fr,
        "Fac": fac,
        "Frac (%)": frac,
    })
    print(tabela.to_string(index=False))
    print(f"\nTotal de observacoes: {total}")
    print(f"Numero de classes: {n_classes}")
    print(f"Amplitude: {amplitude:.2f}")
    print(f"Tamanho da classe (h): {h:.2f}")
    print()
    return tabela


def grafico_barras_anos(df, caminho):
    """Grafico 1: barras com numero de lancamentos por decada."""
    anos = df["Ano"].dropna().astype(int)
    decada = (anos // 10) * 10
    contagem = decada.value_counts().sort_index()

    plt.figure(figsize=(10, 6))
    cores = plt.cm.viridis(np.linspace(0.2, 0.9, len(contagem)))
    barras = plt.bar(contagem.index.astype(str), contagem.values, color=cores, edgecolor="black")

    for barra, valor in zip(barras, contagem.values):
        plt.text(
            barra.get_x() + barra.get_width() / 2,
            barra.get_height() + 20,
            str(valor),
            ha="center",
            fontsize=9,
        )

    plt.title("Lancamentos Espaciais por Decada (1957-2020)", fontsize=14, fontweight="bold")
    plt.xlabel("Decada", fontsize=12)
    plt.ylabel("Numero de Lancamentos", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig(caminho, dpi=150)
    plt.close()
    print(f"Grafico salvo: {caminho}")


def grafico_histograma_custo(df, caminho):
    """Grafico 2: histograma do custo dos foguetes (escala log no Y)."""
    custo = df["CustoFoguete"].dropna()

    plt.figure(figsize=(10, 6))
    plt.hist(
        custo, bins=20, color="#1f77b4", edgecolor="black", alpha=0.85
    )

    media = custo.mean()
    mediana = custo.median()
    plt.axvline(media, color="red", linestyle="--", linewidth=2, label=f"Media: {media:.2f}M USD")
    plt.axvline(mediana, color="green", linestyle="--", linewidth=2, label=f"Mediana: {mediana:.2f}M USD")

    plt.title("Distribuicao do Custo dos Foguetes (Milhoes USD)", fontsize=14, fontweight="bold")
    plt.xlabel("Custo do foguete (milhoes USD)", fontsize=12)
    plt.ylabel("Frequencia (escala log)", fontsize=12)
    plt.yscale("log")
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.6, which="both")
    plt.tight_layout()
    plt.savefig(caminho, dpi=150)
    plt.close()
    print(f"Grafico salvo: {caminho}")


def analise_univariada(serie, titulo):
    """Calcula todas as medidas pedidas pelo briefing."""
    print("=" * 70)
    print(f"ANALISE UNIVARIADA - {titulo}")
    print("=" * 70)

    serie = serie.dropna()
    media = serie.mean()
    mediana = serie.median()
    moda_serie = serie.mode()
    moda = moda_serie.iloc[0] if not moda_serie.empty else float("nan")
    maximo = serie.max()
    minimo = serie.min()
    amplitude = maximo - minimo
    variancia = serie.var()
    desvio = serie.std()
    cv = (desvio / media * 100) if media else float("nan")
    q1 = serie.quantile(0.25)
    q2 = serie.quantile(0.50)
    q3 = serie.quantile(0.75)

    print("Tendencia central:")
    print(f"  Media   : {media:.4f}")
    print(f"  Mediana : {mediana:.4f}")
    print(f"  Moda    : {moda:.4f}")
    print()
    print("Dispersao:")
    print(f"  Maximo            : {maximo:.4f}")
    print(f"  Minimo            : {minimo:.4f}")
    print(f"  Amplitude         : {amplitude:.4f}")
    print(f"  Variancia         : {variancia:.4f}")
    print(f"  Desvio padrao     : {desvio:.4f}")
    print(f"  Coef. de variacao : {cv:.2f}%")
    print()
    print("Separatrizes (quartis):")
    print(f"  Q1 (25%) : {q1:.4f}")
    print(f"  Q2 (50%) : {q2:.4f}")
    print(f"  Q3 (75%) : {q3:.4f}")
    print()
    return {
        "media": media, "mediana": mediana, "moda": moda,
        "maximo": maximo, "minimo": minimo, "amplitude": amplitude,
        "variancia": variancia, "desvio": desvio, "cv": cv,
        "q1": q1, "q2": q2, "q3": q3,
    }


def main():
    print("=" * 70)
    print("ANALISE ESTATISTICA - MISSOES ESPACIAIS 1957-2020")
    print("Equipe AstroTeam - Joao Vitor Belchior e Gabriel Pedro")
    print("=" * 70)
    print()

    df = carregar_dados()
    print(f"Total de missoes na base: {len(df)}")
    print(f"Periodo: {int(df['Ano'].min())} ate {int(df['Ano'].max())}")
    print(f"Missoes com custo informado: {df['CustoFoguete'].notna().sum()}")
    print()

    # Tabelas de frequencia
    tabela_frequencia_discreta(df["Ano"], "Ano de Lancamento")
    tabela_frequencia_continua(df["CustoFoguete"], "Custo do Foguete (milhoes USD)")

    # Graficos
    grafico_barras_anos(df, os.path.join(PASTA_GRAFICOS, "grafico_lancamentos_decada.png"))
    grafico_histograma_custo(df, os.path.join(PASTA_GRAFICOS, "grafico_custo_foguetes.png"))

    # Analises univariadas
    analise_univariada(df["Ano"], "Ano de Lancamento")
    analise_univariada(df["CustoFoguete"], "Custo do Foguete (milhoes USD)")

    print("=" * 70)
    print("FIM DA ANALISE")
    print("=" * 70)


if __name__ == "__main__":
    main()
