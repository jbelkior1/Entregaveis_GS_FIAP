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

### Dados da missão
Os dados ficam numa matriz chamada `dados_missao`, onde cada linha é um ciclo da missão e cada coluna é uma informação monitorada, nesta ordem: temperatura, comunicação, bateria, oxigênio e estabilidade. A missão tem 6 ciclos, que vão de uma situação estável no começo até uma situação crítica no final.

A lista `areas_monitoradas` guarda o nome de cada uma das 5 áreas, usada na hora de montar o relatório.

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

## Vídeo Pitch
Vídeo com o pitch da nossa ideia central para a Global Solution 2026.1, apresentando a proposta da solução Mission Control AI:

https://youtu.be/pzMZWkKNR5Y
