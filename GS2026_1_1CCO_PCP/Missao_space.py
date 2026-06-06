# MISSION SPACE
# Sistema Inteligente de Monitoramento de Missao Espacial
# GS2026.1 - Pensamento Computacional e Automacao com Python
# Integrantes - Nome: João Vitor Belchior  / Gabriel Pedro


NOME_DA_MISSAO = "MISSION CONTROL GS"
NOME_DA_EQUIPE = "AstroTeam"

dados_missao = [
    [23, 95, 90, 97, 92],
    [26, 88, 76, 95, 88],
    [29, 70, 47, 92, 78],
    [33, 58, 35, 88, 66],
    [37, 25, 16, 83, 44],
    [40, 22, 12, 76, 33]
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicacao com a base",
    "Sistema de energia",
    "Suporte de oxigenio",
    "Estabilidade operacional",
]

def analisar_temperatura(t):
    if t < 18:
        return "ATENCAO"
    elif t <= 30:
        return "NORMAL"
    elif t <= 35:
        return "ATENCAO"
    else:
        return "CRITICO"


def analisar_comunicacao(c):
    if c < 30:
        return "CRITICO"
    elif c < 60:
        return "ATENCAO"
    else:
        return "NORMAL"

def analisar_bateria(b):
    if b < 20:
        return "CRITICO"
    elif b < 50:
        return "ATENCAO"
    else:
        return "NORMAL"

def analisar_oxigenio(o):
    if o < 80:
        return "CRITICO"
    elif o < 90:
        return "ATENCAO"
    else:
        return "NORMAL"

def analisar_estabilidade(e):
    if e < 40:
        return "CRITICO"
    elif e < 70:
        return "ATENCAO"
    else:
        return "NORMAL"

def pontuar(classificacao):
    if classificacao == "CRITICO":
        return 2
    elif classificacao == "ATENCAO":
        return 1
    else:
        return 0

def classificar_ciclo(pontos):
    if pontos <= 2:
        return "MISSAO ESTAVEL"
    elif pontos <= 5:
        return "MISSAO EM ATENCAO"
    else:
        return "MISSAO CRITICA"

def analisar_tendencia(primeiro, ultimo):
    if ultimo > primeiro:
        return "A missao apresentou tendencia de piora."
    elif ultimo < primeiro:
        return "A missao apresentou tendencia de melhora."
    else:
        return "A missao permaneceu estavel em relacao ao inicio."

# PROGRAMA PRINCIPAL

print("=" * 50)
print("Missao:", NOME_DA_MISSAO)
print("Equipe:", NOME_DA_EQUIPE)
print("Ciclos analisados:", len(dados_missao))
print("=" * 50)

riscos = []
risco_areas = [0, 0, 0, 0, 0]
soma_temp = 0
soma_com = 0
soma_bat = 0
soma_oxi = 0
soma_est = 0

for i in range(len(dados_missao)):
    ciclo = dados_missao[i]
    temperatura = ciclo[0]
    comunicacao = ciclo[1]
    bateria = ciclo[2]
    oxigenio = ciclo[3]
    estabilidade = ciclo[4]

    c_temp = analisar_temperatura(temperatura)
    c_com = analisar_comunicacao(comunicacao)
    c_bat = analisar_bateria(bateria)
    c_oxi = analisar_oxigenio(oxigenio)
    c_est = analisar_estabilidade(estabilidade)

    p_temp = pontuar(c_temp)
    p_com = pontuar(c_com)
    p_bat = pontuar(c_bat)
    p_oxi = pontuar(c_oxi)
    p_est = pontuar(c_est)

    risco_ciclo = p_temp + p_com + p_bat + p_oxi + p_est

    risco_areas[0] = risco_areas[0] + p_temp
    risco_areas[1] = risco_areas[1] + p_com
    risco_areas[2] = risco_areas[2] + p_bat
    risco_areas[3] = risco_areas[3] + p_oxi
    risco_areas[4] = risco_areas[4] + p_est

    soma_temp = soma_temp + temperatura
    soma_com = soma_com + comunicacao
    soma_bat = soma_bat + bateria
    soma_oxi = soma_oxi + oxigenio
    soma_est = soma_est + estabilidade

    classificacao = classificar_ciclo(risco_ciclo)

    if classificacao == "MISSAO ESTAVEL":
        recomendacao = "Manter operacao normal e continuar monitoramento."
    elif classificacao == "MISSAO EM ATENCAO":
        recomendacao = "Monitorar sistemas em atencao e preparar plano de contingencia."
    else:
        recomendacao = "Acionar protocolos de emergencia e priorizar suporte a vida."

    print()
    print("CICLO", i + 1)
    print("-" * 50)
    print("Temperatura:", temperatura, "C :", c_temp)
    print("Comunicacao:", comunicacao, "% :", c_com)
    print("Bateria:", bateria, "% :", c_bat)
    print("Oxigenio:", oxigenio, "% :", c_oxi)
    print("Estabilidade:", estabilidade, "% :", c_est)
    print("Pontuacao de risco do ciclo :", risco_ciclo)
    print("Classificacao do ciclo :", classificacao)
    print("Recomendacao :", recomendacao)

    riscos.append(risco_ciclo)

n = len(dados_missao)
maior_risco = max(riscos)
ciclo_mais_critico = riscos.index(maior_risco) + 1
risco_medio = sum(riscos) / n

ciclos_criticos = 0
for r in riscos:
    if r >= 6:
        ciclos_criticos = ciclos_criticos + 1


indice_area = 0
for i in range(len(risco_areas)):
    if risco_areas[i] > risco_areas[indice_area]:
        indice_area = i
area_mais_afetada = areas_monitoradas[indice_area]

tendencia = analisar_tendencia(riscos[0], riscos[-1])
classificacao_final = classificar_ciclo(risco_medio)

print()
print("=" * 50)
print("RELATORIO FINAL DA MISSAO")
print("=" * 50)
print("Missao:", NOME_DA_MISSAO)
print("Equipe:", NOME_DA_EQUIPE)
print("Ciclos analisados:", n)
print()
print("Media de temperatura:", round(soma_temp / n, 2), "C")
print("Media de comunicacao:", round(soma_com / n, 2), "%")
print("Media de bateria:", round(soma_bat / n, 2), "%")
print("Media de oxigenio:", round(soma_oxi / n, 2), "%")
print("Media de estabilidade:", round(soma_est / n, 2), "%")
print()
print("Ciclo mais critico: Ciclo", ciclo_mais_critico)
print("Maior pontuacao de risco:", maior_risco)
print("Risco medio da missao:", round(risco_medio, 2))
print("Quantidade de ciclos criticos:", ciclos_criticos)
print()
print("Tendencia da missao:", tendencia)
print()
print("Pontuacao acumulada por area:")
for i in range(len(areas_monitoradas)):
    print(areas_monitoradas[i], risco_areas[i], "pontos")
print()
print("Area mais afetada:", area_mais_afetada)
print("Classificacao final da missao:", classificacao_final)
