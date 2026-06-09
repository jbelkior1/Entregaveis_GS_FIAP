# Analise Estatistica - Missoes Espaciais

**Global Solution 2026.1 - Modelagem Linear para Aprendizado de Maquina**

Analise estatistica descritiva sobre o historico de missoes espaciais (1957-2020), aplicada ao tema da Global Solution 2026.1.

## Equipe AstroTeam
- João Vitor Belchior - RM: 572478
- Gabriel Pedro de Souza - RM: 571995

## Arquivos
- `dados.csv` - base de dados real (4.324 missoes)
- `analise.py` - codigo Python com tabelas de frequencia, graficos e analises univariadas
- `gerar_relatorio.py` - script que gera o PDF final
- `relatorio.pdf` - relatorio estatistico completo
- `graficos/` - graficos gerados pelo script

## Base de dados
**All Space Missions from 1957** - historico publico de lancamentos espaciais extraido de nextspaceflight.com, com 4.324 missoes registradas. Variaveis usadas:
- Ano de lancamento (quantitativa discreta)
- Custo do foguete em milhoes USD (quantitativa continua)

Fonte: https://github.com/camille-004/space-race-viz/blob/master/Space_Corrected.csv

## Como executar
```
python analise.py          # roda a analise no terminal e gera os graficos
python gerar_relatorio.py  # gera o relatorio.pdf
```

Requer Python 3.10+ com `pandas`, `matplotlib`, `numpy` e `reportlab`.

## O que o relatorio contem
- Tabela de distribuicao de frequencia para variavel discreta (ano)
- Tabela de distribuicao de frequencia para variavel continua (custo) com regra de Sturges
- 2 graficos: barras por decada e histograma do custo (escala log)
- Medidas de tendencia central: media, mediana, moda
- Medidas de dispersao: maximo, minimo, amplitude, variancia, desvio padrao, CV
- Medidas separatrizes: quartis Q1, Q2, Q3
- Interpretacoes e insights aplicados ao tema da Global Solution
