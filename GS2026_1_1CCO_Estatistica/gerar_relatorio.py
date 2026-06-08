# GS2026.1 - Gerador do relatorio estatistico (PDF)
# Equipe AstroTeam
# Joao Vitor Belchior - RM: 572478
# Gabriel Pedro de Souza - RM: 571995

import os
import pandas as pd
import numpy as np
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak,
)

import analise as A

PASTA = os.path.dirname(os.path.abspath(__file__))
PDF_PATH = os.path.join(PASTA, "relatorio.pdf")
PASTA_GRAFICOS = os.path.join(PASTA, "graficos")


def estilos():
    base = getSampleStyleSheet()
    base.add(ParagraphStyle(
        name="JustText", parent=base["BodyText"],
        alignment=TA_JUSTIFY, fontSize=11, leading=15, spaceAfter=8,
    ))
    base.add(ParagraphStyle(
        name="CapaTitulo", parent=base["Title"],
        alignment=TA_CENTER, fontSize=22, leading=28, spaceAfter=14,
    ))
    base.add(ParagraphStyle(
        name="CapaSub", parent=base["Title"],
        alignment=TA_CENTER, fontSize=14, leading=18, spaceAfter=10,
        textColor=colors.HexColor("#444444"),
    ))
    base.add(ParagraphStyle(
        name="SecH1", parent=base["Heading1"],
        fontSize=16, spaceBefore=14, spaceAfter=10,
        textColor=colors.HexColor("#1f3a5f"),
    ))
    base.add(ParagraphStyle(
        name="SecH2", parent=base["Heading2"],
        fontSize=13, spaceBefore=10, spaceAfter=6,
        textColor=colors.HexColor("#1f3a5f"),
    ))
    return base


def tabela_para_flowable(df_tabela, fontsize=8):
    """Converte um DataFrame em um Table do reportlab."""
    dados = [list(df_tabela.columns)] + df_tabela.astype(str).values.tolist()
    t = Table(dados, repeatRows=1, hAlign="CENTER")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1f3a5f")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), fontsize),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.grey),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f0f4f9")]),
    ]))
    return t


def tabela_medidas(stats, fontsize=10):
    dados = [
        ["Medida", "Valor"],
        ["Media", f"{stats['media']:.4f}"],
        ["Mediana", f"{stats['mediana']:.4f}"],
        ["Moda", f"{stats['moda']:.4f}"],
        ["Maximo", f"{stats['maximo']:.4f}"],
        ["Minimo", f"{stats['minimo']:.4f}"],
        ["Amplitude", f"{stats['amplitude']:.4f}"],
        ["Variancia", f"{stats['variancia']:.4f}"],
        ["Desvio padrao", f"{stats['desvio']:.4f}"],
        ["Coef. de variacao", f"{stats['cv']:.2f}%"],
        ["Q1 (25%)", f"{stats['q1']:.4f}"],
        ["Q2 (50%)", f"{stats['q2']:.4f}"],
        ["Q3 (75%)", f"{stats['q3']:.4f}"],
    ]
    t = Table(dados, colWidths=[6 * cm, 5 * cm], hAlign="CENTER")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1f3a5f")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), fontsize),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.grey),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f0f4f9")]),
    ]))
    return t


def calcular_stats(serie):
    serie = serie.dropna()
    return {
        "media": serie.mean(),
        "mediana": serie.median(),
        "moda": serie.mode().iloc[0] if not serie.mode().empty else float("nan"),
        "maximo": serie.max(),
        "minimo": serie.min(),
        "amplitude": serie.max() - serie.min(),
        "variancia": serie.var(),
        "desvio": serie.std(),
        "cv": serie.std() / serie.mean() * 100 if serie.mean() else float("nan"),
        "q1": serie.quantile(0.25),
        "q2": serie.quantile(0.50),
        "q3": serie.quantile(0.75),
    }


def construir_pdf():
    df = A.carregar_dados()
    st = estilos()
    story = []

    # ----- CAPA -----
    story.append(Spacer(1, 3 * cm))
    story.append(Paragraph("Relatorio Estatistico", st["CapaTitulo"]))
    story.append(Paragraph("Missoes Espaciais (1957-2020)", st["CapaSub"]))
    story.append(Spacer(1, 1 * cm))
    story.append(Paragraph(
        "Global Solution 2026.1 - Modelagem Linear para Aprendizado de Maquina",
        st["CapaSub"],
    ))
    story.append(Spacer(1, 3 * cm))
    story.append(Paragraph("<b>Equipe AstroTeam</b>", st["CapaSub"]))
    story.append(Paragraph("Joao Vitor Belchior - RM: 572478", st["CapaSub"]))
    story.append(Paragraph("Gabriel Pedro de Souza - RM: 571995", st["CapaSub"]))
    story.append(Spacer(1, 3 * cm))
    story.append(Paragraph("FIAP - 1CCO - 1o ano de Ciencia da Computacao", st["CapaSub"]))
    story.append(PageBreak())

    # ----- 1. INTRODUCAO -----
    story.append(Paragraph("1. Introducao", st["SecH1"]))
    story.append(Paragraph(
        "A Global Solution 2026.1 traz como tema o monitoramento de missoes espaciais "
        "experimentais. A proposta da disciplina e usar dados reais para entender melhor "
        "como o setor espacial se comporta, e a partir disso gerar informacao util para "
        "apoiar a tomada de decisao em uma empresa ou cliente do segmento.",
        st["JustText"],
    ))
    story.append(Paragraph(
        "Para este trabalho escolhemos analisar o historico de lancamentos espaciais "
        "feitos no mundo entre 1957 e 2020. A ideia foi aplicar os conceitos de "
        "estatistica descritiva vistos em aula sobre uma base publica real, montando "
        "tabelas de distribuicao de frequencia, gerando graficos e calculando as "
        "principais medidas (tendencia central, dispersao e separatrizes).",
        st["JustText"],
    ))
    story.append(Paragraph(
        "O relatorio esta organizado em sete secoes: descricao da base de dados, tabelas "
        "de frequencia (uma variavel discreta e uma continua), graficos, analises "
        "univariadas, discussao dos resultados e conclusao final com os principais "
        "insights extraidos.",
        st["JustText"],
    ))

    # ----- 2. BASE DE DADOS -----
    story.append(Paragraph("2. Base de Dados", st["SecH1"]))
    story.append(Paragraph(
        "A base usada foi a <b>All Space Missions from 1957</b>, disponivel publicamente "
        "no GitHub e originalmente extraida do site nextspaceflight.com. Ela traz o "
        "registro de 4.324 lancamentos espaciais, com informacoes da empresa responsavel "
        "(SpaceX, NASA, Roscosmos, CASC, entre outras), local de lancamento, data, "
        "detalhes do foguete e da missao, status do foguete (ativo ou aposentado), "
        "custo do foguete em milhoes de dolares e status da missao (sucesso ou falha).",
        st["JustText"],
    ))
    story.append(Paragraph(
        "Escolhemos essa base porque ela bate diretamente com o tema da GS, e porque "
        "tem variaveis quantitativas adequadas para os dois tipos de analise pedidos "
        "(uma discreta e uma continua). Alem disso, e uma base ja consolidada e usada "
        "em diversos trabalhos academicos sobre o setor espacial.",
        st["JustText"],
    ))
    story.append(Paragraph("<b>Variaveis selecionadas:</b>", st["JustText"]))
    story.append(Paragraph(
        "<b>Ano de lancamento</b> - variavel quantitativa discreta. Foi extraida do "
        "campo de data original. Indica em qual ano cada missao foi realizada.",
        st["JustText"],
    ))
    story.append(Paragraph(
        "<b>Custo do foguete (milhoes USD)</b> - variavel quantitativa continua. "
        "Esta disponivel em 964 das 4.324 missoes da base (o que representa cerca de "
        "22%). Como o custo so e informado para parte das missoes, trabalhamos com esse "
        "subconjunto na analise da variavel continua.",
        st["JustText"],
    ))
    story.append(PageBreak())

    # ----- 3. TABELAS DE FREQUENCIA -----
    story.append(Paragraph("3. Tabelas de Distribuicao de Frequencia", st["SecH1"]))
    story.append(Paragraph(
        "A tabela de distribuicao de frequencia organiza os dados em uma estrutura que "
        "facilita a leitura. Em cada linha aparecem os seguintes valores: Fi (frequencia "
        "absoluta, ou seja, quantas vezes o valor aparece na base), Fr (frequencia "
        "relativa em percentual, ou seja, qual a participacao desse valor no total), "
        "Fac (frequencia acumulada, somando as Fi linha a linha) e Frac (frequencia "
        "acumulada relativa em percentual).",
        st["JustText"],
    ))

    story.append(Paragraph("3.1. Variavel discreta - Ano de lancamento", st["SecH2"]))
    story.append(Paragraph(
        "Como o ano de lancamento e uma variavel discreta, cada valor possivel (1957, "
        "1958, ... 2020) ocupa uma linha da tabela. A frequencia absoluta indica quantos "
        "lancamentos foram feitos naquele ano.",
        st["JustText"],
    ))
    tab_ano = A.tabela_frequencia_discreta(df["Ano"], "Ano de Lancamento")
    story.append(tabela_para_flowable(tab_ano, fontsize=7))
    story.append(Spacer(1, 0.4 * cm))
    story.append(Paragraph(
        "<b>Interpretacao:</b> a tabela mostra que a atividade espacial nao foi "
        "constante ao longo do tempo. No comeco da corrida espacial (entre 1957 e 1964) "
        "o numero de lancamentos era baixo, com poucos ensaios pioneiros por ano. A "
        "partir de 1965 o volume cresce de forma rapida e a decada de 1970 concentra o "
        "auge da atividade, com varios anos passando de 100 missoes (1967, 1968, 1969, "
        "1970, 1971, 1975, 1976 e 1977). O pico isolado dessa fase foi 1971, com 116 "
        "lancamentos.",
        st["JustText"],
    ))
    story.append(Paragraph(
        "Apos 1978 a quantidade de lancamentos por ano cai e fica estavel em torno de "
        "50 a 70 missoes ate por volta de 2015. A partir de 2016 ha uma nova alta, com "
        "2018 sendo o ano de maior frequencia de toda a base (117 lancamentos). Esse "
        "movimento recente reflete a entrada de empresas privadas no setor, como a "
        "SpaceX, e o crescimento da industria espacial chinesa.",
        st["JustText"],
    ))
    story.append(PageBreak())

    story.append(Paragraph("3.2. Variavel continua - Custo do foguete", st["SecH2"]))
    story.append(Paragraph(
        "Como o custo do foguete tem muitos valores diferentes, o jeito de montar a "
        "tabela e agrupar os valores em faixas. Aqui, escolhemos dividir os custos em "
        "5 faixas de tamanho igual e contar quantos foguetes caem em cada uma.",
        st["JustText"],
    ))
    tab_custo = A.tabela_frequencia_continua(
        df["CustoFoguete"], "Custo do Foguete (milhoes USD)", n_classes=5,
    )
    story.append(tabela_para_flowable(tab_custo, fontsize=9))
    story.append(Spacer(1, 0.4 * cm))
    story.append(Paragraph(
        "<b>Interpretacao:</b> quase tudo (98,4%) cai na primeira faixa, que vai ate "
        "cerca de 1 bilhao de USD. Ou seja, a maioria dos foguetes lancados na historia "
        "custou bem menos do que isso. As faixas seguintes ficam quase vazias e mostram "
        "que poucos foguetes sao muito caros - aparecem so 13 lancamentos perto de "
        "1 bilhao (foguetes pesados como Saturno V e Space Shuttle) e 2 lancamentos no "
        "topo, perto de 5 bilhoes (outliers do programa Apollo).",
        st["JustText"],
    ))

    # ----- 4. GRAFICOS -----
    story.append(PageBreak())
    story.append(Paragraph("4. Graficos", st["SecH1"]))
    story.append(Paragraph(
        "Para visualizar os dados de forma mais intuitiva, geramos dois graficos "
        "distintos, com variaveis diferentes. Cada um inclui titulo, rotulos nos "
        "eixos X e Y, cores e elementos auxiliares (grade, valores rotulados, linhas "
        "de referencia) que ajudam a leitura.",
        st["JustText"],
    ))

    story.append(Paragraph("4.1. Grafico de barras - Lancamentos por decada", st["SecH2"]))
    story.append(Paragraph(
        "O primeiro grafico agrupa a variavel discreta (ano) por decada. Optamos por "
        "trabalhar com decadas em vez de anos para que o grafico de barras fique mais "
        "legivel: 8 barras (uma para cada decada de 1950 a 2020) em vez de 64 (uma "
        "para cada ano). Cada barra mostra o numero total de lancamentos da decada.",
        st["JustText"],
    ))
    img1 = os.path.join(PASTA_GRAFICOS, "grafico_lancamentos_decada.png")
    story.append(Image(img1, width=16 * cm, height=9.6 * cm))
    story.append(Spacer(1, 0.3 * cm))
    story.append(Paragraph(
        "<b>Interpretacao:</b> o grafico confirma o que a tabela ja sugeria. A decada "
        "de 1970 e a com mais lancamentos (983 missoes), seguida pelos anos 1960 "
        "(752) e 2010 (657). A decada de 2000 e a com menor volume entre as decadas "
        "completas (464 lancamentos), e a decada de 2020 aparece com apenas 63 porque "
        "a base se encerra em agosto de 2020.",
        st["JustText"],
    ))
    story.append(Paragraph(
        "A leitura visual deixa claro tres ciclos do setor: a fase pioneira (anos 1950), "
        "o auge (1960-1970), uma queda gradual (1980-2000) e uma retomada nas duas "
        "ultimas decadas. Esse padrao reflete momentos historicos importantes como a "
        "corrida espacial e o fim do programa Apollo.",
        st["JustText"],
    ))

    story.append(PageBreak())
    story.append(Paragraph("4.2. Histograma - Distribuicao do custo dos foguetes", st["SecH2"]))
    story.append(Paragraph(
        "O segundo grafico e um histograma da variavel continua (custo do foguete em "
        "milhoes de USD). Usamos 20 intervalos para a divisao das barras. Como a "
        "distribuicao e muito desigual (quase tudo se concentra na faixa inicial), "
        "aplicamos uma escala logaritmica no eixo Y. Sem a escala log, as barras "
        "menores ficariam invisiveis no grafico, e a escala log permite enxergar tanto "
        "a faixa dominante quanto os grupos minoritarios.",
        st["JustText"],
    ))
    img2 = os.path.join(PASTA_GRAFICOS, "grafico_custo_foguetes.png")
    story.append(Image(img2, width=16 * cm, height=9.6 * cm))
    story.append(Spacer(1, 0.3 * cm))
    story.append(Paragraph(
        "<b>Interpretacao:</b> tres regioes ficam visiveis. A primeira, entre 0 e 500 "
        "milhoes de USD, concentra a grande maioria dos foguetes (mais de 800 na "
        "primeira barra). A segunda regiao, em torno de 1 bilhao de USD, mostra os "
        "foguetes pesados (Saturno V e Shuttle), com cerca de 13 ocorrencias. A "
        "terceira regiao, no extremo direito (proximo a 5 bilhoes), tem 2 outliers "
        "isolados.",
        st["JustText"],
    ))
    story.append(Paragraph(
        "A linha vermelha marca a media (153,79M USD) e a linha verde a mediana "
        "(62,00M USD). A diferenca entre essas duas linhas e visivel mesmo no grafico "
        "e confirma a assimetria a direita: a media e puxada para cima pelos foguetes "
        "muito caros, enquanto a mediana fica mais perto do custo tipico real.",
        st["JustText"],
    ))

    # ----- 5. ANALISE UNIVARIADA -----
    story.append(PageBreak())
    story.append(Paragraph("5. Analises Univariadas", st["SecH1"]))
    story.append(Paragraph(
        "A analise univariada calcula medidas estatisticas para uma unica variavel "
        "por vez. Para cada uma das duas variaveis escolhidas, calculamos: medidas de "
        "tendencia central (media, mediana e moda), medidas de dispersao (maximo, "
        "minimo, amplitude, variancia, desvio padrao e coeficiente de variacao) e as "
        "separatrizes (quartis Q1, Q2 e Q3).",
        st["JustText"],
    ))

    stats_ano = calcular_stats(df["Ano"])
    stats_custo = calcular_stats(df["CustoFoguete"])

    story.append(Paragraph("5.1. Ano de lancamento", st["SecH2"]))
    story.append(tabela_medidas(stats_ano))
    story.append(Spacer(1, 0.4 * cm))
    story.append(Paragraph(
        "<b>Interpretacao das medidas de tendencia central:</b> a media (1987) e a "
        "mediana (1985) ficaram muito proximas, com diferenca de apenas dois anos. "
        "Isso indica que a distribuicao dos lancamentos no tempo e quase simetrica em "
        "torno do meio da decada de 1980. A moda em 2018 mostra qual o ano com mais "
        "lancamentos da base (117 missoes), e e um indicador interessante de que o "
        "ano mais movimentado e recente.",
        st["JustText"],
    ))
    story.append(Paragraph(
        "<b>Interpretacao das medidas de dispersao:</b> o maximo (2020) e o minimo "
        "(1957) dao a amplitude total de 63 anos. A variancia (327) e o desvio padrao "
        "(18 anos) indicam o quanto os anos de lancamento variam em torno da media. "
        "O coeficiente de variacao de apenas 0,91% mostra dispersao muito baixa em "
        "termos percentuais, o que faz sentido para uma variavel ano (que naturalmente "
        "tem pequena variacao percentual em torno de uma media na casa de 1900).",
        st["JustText"],
    ))
    story.append(Paragraph(
        "<b>Interpretacao das separatrizes:</b> os quartis dividem os dados em quatro "
        "partes iguais. Q1 = 1972 indica que 25% das missoes ocorreram ate 1972. "
        "Q2 = 1985 (que e a mediana) mostra que metade das missoes ocorreu ate 1985. "
        "Q3 = 2002 indica que 75% das missoes ocorreram ate 2002. Ou seja, 50% das "
        "missoes da base foram realizadas entre 1972 e 2002, periodo que concentra a "
        "maior parte da atividade espacial historica.",
        st["JustText"],
    ))

    story.append(PageBreak())
    story.append(Paragraph("5.2. Custo do foguete (milhoes USD)", st["SecH2"]))
    story.append(tabela_medidas(stats_custo))
    story.append(Spacer(1, 0.4 * cm))
    story.append(Paragraph(
        "<b>Interpretacao das medidas de tendencia central:</b> aqui a media (153,79M "
        "USD) e quase 2,5 vezes maior que a mediana (62,00M USD). Essa diferenca grande "
        "entre as duas e o indicador classico de assimetria a direita: alguns valores "
        "muito altos puxam a media para cima, enquanto a mediana fica representando o "
        "valor central real. Nesse caso, a mediana e a medida mais adequada para "
        "descrever o custo tipico de um foguete. A moda em 450M USD identifica o valor "
        "que mais se repete na base.",
        st["JustText"],
    ))
    story.append(Paragraph(
        "<b>Interpretacao das medidas de dispersao:</b> os custos vao de 5,30M USD "
        "(foguete mais barato) ate 5.000M USD (mais caro), o que da uma amplitude de "
        "4.994,70 milhoes. A variancia (83.203,82) e o desvio padrao (288,45M USD) "
        "indicam que os custos sao muito espalhados em torno da media. O coeficiente "
        "de variacao de 187,56% e extremamente alto - acima de 30% ja se considera "
        "que a dispersao e grande. Esse CV gigante confirma que o custo dos foguetes "
        "e altamente heterogeneo e que a media isolada nao representa bem a realidade.",
        st["JustText"],
    ))
    story.append(Paragraph(
        "<b>Interpretacao das separatrizes:</b> Q1 = 40M USD significa que 25% dos "
        "foguetes custam ate 40 milhoes. Q2 = 62M USD (mediana) mostra que metade dos "
        "foguetes custa ate 62 milhoes. Q3 = 164M USD indica que 75% dos foguetes "
        "custam ate 164 milhoes. O intervalo interquartil (Q3 - Q1 = 124M USD) "
        "representa onde estao concentrados os 50% centrais dos custos, ou seja, a "
        "faixa tipica de mercado e entre 40M e 164M USD.",
        st["JustText"],
    ))

    # ----- 6. DISCUSSAO -----
    story.append(PageBreak())
    story.append(Paragraph("6. Discussao dos Resultados", st["SecH1"]))
    story.append(Paragraph(
        "Cruzando as informacoes das duas variaveis analisadas, da para tirar algumas "
        "leituras interessantes do setor espacial.",
        st["JustText"],
    ))
    story.append(Paragraph(
        "<b>Sobre o volume de lancamentos:</b> o setor espacial nunca operou em ritmo "
        "constante. O pico historico foi nos anos 1970, durante a corrida espacial "
        "entre EUA e Uniao Sovietica. Depois do fim do programa Apollo, o ritmo caiu "
        "e a atividade ficou concentrada em poucas agencias estatais. A partir de 2016, "
        "com a entrada da SpaceX e da industria chinesa, ha uma nova fase de "
        "crescimento, que provavelmente vai se acentuar nas proximas decadas.",
        st["JustText"],
    ))
    story.append(Paragraph(
        "<b>Sobre o custo dos foguetes:</b> a distribuicao e altamente assimetrica. "
        "A grande maioria dos foguetes (98%) custa menos de 460M USD, e essa e a faixa "
        "que define o mercado padrao. Os foguetes pesados (perto de 1 bilhao) e os "
        "outliers historicos (5 bilhoes) sao excecoes. Para uma analise pratica, e "
        "mais util olhar para a mediana e para o intervalo interquartil do que para a "
        "media, que e enviesada pelos outliers.",
        st["JustText"],
    ))
    story.append(Paragraph(
        "<b>Aplicacao pratica para uma empresa do setor:</b> se uma empresa precisa "
        "estimar o orcamento de um novo lancamento de medio porte, o intervalo entre "
        "Q1 (40M USD) e Q3 (164M USD) e um ponto de partida realista, pois cobre 50% "
        "dos casos historicos. Para lancamentos pesados, o referencial sobe para a "
        "faixa de 1 bilhao. Os outliers de 5 bilhoes sao casos especificos do programa "
        "Apollo e nao representam o mercado atual.",
        st["JustText"],
    ))
    story.append(Paragraph(
        "<b>Limitacoes da analise:</b> a variavel de custo so esta disponivel em "
        "964 das 4.324 missoes (cerca de 22%), entao as conclusoes sobre custo se "
        "baseiam nesse subconjunto. Tambem vale destacar que os valores estao em USD "
        "historico, sem ajuste de inflacao - um foguete de 100M USD em 1965 nao tem o "
        "mesmo poder de compra que 100M USD em 2020. Para um trabalho mais rigoroso, "
        "uma proxima etapa seria fazer essa correcao.",
        st["JustText"],
    ))

    # ----- 7. CONCLUSAO -----
    story.append(PageBreak())
    story.append(Paragraph("7. Conclusao", st["SecH1"]))
    story.append(Paragraph(
        "A analise estatistica realizada sobre as 4.324 missoes espaciais entre 1957 "
        "e 2020 cumpriu o objetivo de transformar dados brutos em informacao util. "
        "Os principais achados sao:",
        st["JustText"],
    ))
    story.append(Paragraph(
        "1. A atividade espacial passou por tres ciclos: pico nos anos 1970 (983 "
        "missoes na decada), retracao entre 1980 e 2015, e nova expansao a partir "
        "de 2016. O ano de 2018 e o mais movimentado de toda a base (117 lancamentos).",
        st["JustText"],
    ))
    story.append(Paragraph(
        "2. O custo dos foguetes tem distribuicao assimetrica a direita. A mediana "
        "(62M USD) representa o custo tipico melhor do que a media (154M USD), que e "
        "puxada por outliers como o Saturno V e o Space Shuttle.",
        st["JustText"],
    ))
    story.append(Paragraph(
        "3. O intervalo interquartil (40M a 164M USD) define a faixa de mercado de "
        "foguetes de medio porte, e pode ser usado como referencia para estimativas "
        "iniciais de orcamento em uma nova missao.",
        st["JustText"],
    ))
    story.append(Paragraph(
        "4. O coeficiente de variacao de 187,56% para o custo confirma que o mercado "
        "e extremamente heterogeneo, com produtos muito diferentes em escala - desde "
        "lancadores pequenos ate foguetes super pesados de missoes tripuladas.",
        st["JustText"],
    ))
    story.append(Spacer(1, 0.6 * cm))
    story.append(Paragraph(
        "Aplicado ao tema da Global Solution 2026.1, esse tipo de analise serve para "
        "calibrar regras realistas em um sistema de monitoramento como o Mission "
        "Control AI: define faixas plausiveis de custo, mostra os ciclos de atividade "
        "do setor e ajuda a empresa ou cliente a entender o contexto historico antes "
        "de tomar decisoes sobre uma nova missao.",
        st["JustText"],
    ))

    # ----- REFERENCIAS -----
    story.append(PageBreak())
    story.append(Paragraph("8. Referencias", st["SecH1"]))
    story.append(Paragraph(
        "Base de dados: All Space Missions from 1957. Disponivel em: "
        "https://github.com/camille-004/space-race-viz/blob/master/Space_Corrected.csv "
        "(originalmente extraida de nextspaceflight.com).",
        st["JustText"],
    ))
    story.append(Paragraph(
        "Material da disciplina Modelagem Linear para Aprendizado de Maquina - FIAP, "
        "Global Solution 2026.1.",
        st["JustText"],
    ))
    story.append(Paragraph(
        "Bibliotecas Python utilizadas: pandas (manipulacao de dados), numpy (calculos "
        "numericos), matplotlib (graficos), reportlab (geracao do PDF).",
        st["JustText"],
    ))
    story.append(Paragraph(
        "Regra de Sturges para calculo do numero de classes em distribuicao de "
        "frequencia continua: k = 1 + 3,322 x log10(n).",
        st["JustText"],
    ))

    # ----- BUILD -----
    doc = SimpleDocTemplate(
        PDF_PATH, pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm,
        topMargin=2 * cm, bottomMargin=2 * cm,
        title="Relatorio Estatistico - Missoes Espaciais",
        author="AstroTeam",
    )
    doc.build(story)
    print(f"PDF gerado: {PDF_PATH}")


if __name__ == "__main__":
    construir_pdf()
