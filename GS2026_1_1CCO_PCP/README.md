# Mission Control AI

**Global Solution 2026.1 - Pensamento Computacional e Automação com Python**

Sistema em Python que simula o monitoramento de uma missão espacial. O programa guarda os dados de vários ciclos da missão numa matriz, analisa cada ciclo, gera alertas automáticos e no final mostra um relatório com a situação geral da operação.

## Equipe AstroTeam (Dupla)
- João Vitor Belchior Domingos Leite - RM: 572478
- Gabriel Pedro de Souza - RM: 571995

## Como executar
```
python Missao_space.py
```
Não precisa instalar nada além do Python. É só rodar e o relatório aparece no terminal.

## Como o sistema está organizado

### Dados da missão (a matriz)
Os dados ficam numa matriz chamada `dados_missao`, que é uma lista de listas. Cada linha é um ciclo da missão (um momento no tempo) e cada coluna é uma informação monitorada, sempre nesta ordem: temperatura, comunicação, bateria, oxigênio e estabilidade.

```
dados_missao = [
    [23, 95, 90, 97, 92],   # Ciclo 1 - tudo normal, missao saudavel
    [26, 88, 76, 95, 88],   # Ciclo 2 - ainda estavel
    [29, 70, 47, 92, 78],   # Ciclo 3 - bateria comeca a cair
    [33, 58, 35, 88, 66],   # Ciclo 4 - varios sistemas em atencao
    [37, 25, 16, 83, 44],   # Ciclo 5 - temperatura, comunicacao e bateria criticas
    [40, 22, 12, 76, 33]    # Ciclo 6 - missao em estado critico
]
```

A ideia é que a missão começa saudável (Ciclo 1) e vai se degradando com o tempo até chegar a um estado crítico (Ciclo 6). Lendo de cima para baixo dá para acompanhar a temperatura subindo e a comunicação, bateria, oxigênio e estabilidade caindo.

Para pegar um valor específico usamos os índices da matriz: `dados_missao[0][0]` é a temperatura do primeiro ciclo (23), `dados_missao[4][2]` é a bateria do quinto ciclo (16), e assim por diante. No programa, o laço percorre linha por linha e separa as 5 colunas de cada ciclo.

A lista `areas_monitoradas` guarda o nome de cada uma das 5 colunas ("Temperatura interna", "Comunicacao com a base", etc.), usada na hora de montar o relatório final.

### Funções de análise
Cada informação tem uma função própria que recebe o valor e devolve a classificação (NORMAL, ATENÇÃO ou CRÍTICO):
- `analisar_temperatura()`
- `analisar_comunicacao()`
- `analisar_bateria()`
- `analisar_oxigenio()`
- `analisar_estabilidade()`

Essas funções usam `if`/`elif`/`else` para comparar o valor com os limites de cada faixa.

### Pontuação e classificação
- `pontuar()` transforma a classificação em pontos: NORMAL = 0, ATENÇÃO = 1, CRÍTICO = 2.
- `classificar_ciclo()` soma os pontos do ciclo e devolve se a missão está ESTÁVEL, EM ATENÇÃO ou CRÍTICA.
- `analisar_tendencia()` compara o risco do primeiro ciclo com o do último para dizer se a missão melhorou, piorou ou ficou estável.

### Programa principal
Um laço `for` percorre todos os ciclos da matriz. Para cada ciclo o programa:
1. Separa os 5 valores do ciclo.
2. Classifica cada um com as funções de análise.
3. Soma a pontuação de risco do ciclo.
4. Acumula a pontuação por área e a soma de cada métrica (para as médias).
5. Mostra o resultado do ciclo com a recomendação.

Depois do laço, o programa calcula o ciclo mais crítico, o risco médio, a quantidade de ciclos críticos, a tendência da missão e qual área acumulou mais risco. Tudo isso é exibido no relatório final no terminal.

## Regras de alerta

| Parâmetro | NORMAL (0 pts) | ATENÇÃO (1 pt) | CRÍTICO (2 pts) |
| :--- | :--- | :--- | :--- |
| Temperatura | 18°C a 30°C | < 18°C ou 31°C a 35°C | > 35°C |
| Comunicação | ≥ 60% | 30% a 59% | < 30% |
| Bateria | ≥ 50% | 20% a 49% | < 20% |
| Oxigênio | ≥ 90% | 80% a 89% | < 80% |
| Estabilidade | ≥ 70% | 40% a 69% | < 40% |

## Classificação do ciclo
Como cada ciclo tem 5 informações e cada uma vale no máximo 2 pontos, a pontuação de um ciclo vai de 0 a 10:
- 0 a 2 pontos: MISSÃO ESTÁVEL
- 3 a 5 pontos: MISSÃO EM ATENÇÃO
- 6 a 10 pontos: MISSÃO CRÍTICA

## Devolução no terminal
Quando o programa roda, ele mostra primeiro a análise de cada ciclo e depois um relatório final. Seguindo a nossa matriz, o terminal devolve assim:

```
CICLO 1
--------------------------------------------------
Temperatura: 23 C : NORMAL
Comunicacao: 95 % : NORMAL
Bateria: 90 % : NORMAL
Oxigenio: 97 % : NORMAL
Estabilidade: 92 % : NORMAL
Pontuacao de risco do ciclo : 0
Classificacao do ciclo : MISSAO ESTAVEL
Recomendacao : Manter operacao normal e continuar monitoramento.
```

No Ciclo 1 todos os valores estão dentro do NORMAL, então a pontuação de risco é 0 e a missão fica ESTÁVEL. Conforme os ciclos avançam, os valores pioram e a pontuação sobe. No Ciclo 6, por exemplo, todas as 5 áreas ficam CRÍTICAS, a pontuação chega no máximo (10) e a missão é classificada como CRÍTICA.

Depois de passar por todos os ciclos, o programa junta tudo e mostra o relatório final:

```
==================================================
RELATORIO FINAL DA MISSAO
==================================================
Missao: MISSION CONTROL GS
Equipe: AstroTeam
Ciclos analisados: 6

Media de temperatura: 31.33 C
Media de comunicacao: 59.67 %
Media de bateria: 46.0 %
Media de oxigenio: 88.5 %
Media de estabilidade: 66.83 %

Ciclo mais critico: Ciclo 6
Maior pontuacao de risco: 10
Risco medio da missao: 4.0
Quantidade de ciclos criticos: 2

Tendencia da missao: A missao apresentou tendencia de piora.

Pontuacao acumulada por area:
Temperatura interna 5 pontos
Comunicacao com a base 5 pontos
Sistema de energia 6 pontos
Suporte de oxigenio 4 pontos
Estabilidade operacional 4 pontos

Area mais afetada: Sistema de energia
Classificacao final da missao: MISSAO EM ATENCAO
```

O relatório final segue a nossa linha de raciocínio: como a missão começou em 0 de risco (Ciclo 1) e terminou em 10 (Ciclo 6), a tendência é de **piora**. Somando o risco de cada área ao longo dos 6 ciclos, o "Sistema de energia" (a bateria) é o que mais acumulou pontos (6), então é apontado como a **área mais afetada**. E como o risco médio da missão ficou em 4.0, a classificação final é MISSÃO EM ATENÇÃO.

## Vídeo Pitch
Vídeo com o pitch da nossa ideia central para a Global Solution 2026.1, apresentando a proposta da solução Mission Control AI:

https://youtu.be/pzMZWkKNR5Y
