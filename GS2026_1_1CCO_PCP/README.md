# Mission Control AI

**Global Solution 2026.1 - Pensamento Computacional e Automação com Python**

Sistema em Python que simula o monitoramento de uma missão espacial. O programa percorre 6 ciclos de telemetria, analisa cada um, gera alertas e mostra um relatório final no terminal.

## Equipe AstroTeam (Dupla)
- João Vitor Belchior Domingos Leite - RM: 572478
- Gabriel Pedro de Souza - RM: 571995

## Como executar
```
python Missao_space.py
```

## O que o sistema faz
A cada ciclo o programa analisa 5 áreas da missão:
- Temperatura interna
- Comunicação com a base
- Sistema de energia
- Suporte de oxigênio
- Estabilidade operacional

Calcula a pontuação de risco do ciclo, classifica a situação e gera uma recomendação. No final mostra a média de cada métrica, o ciclo mais crítico, a tendência da missão (melhora ou piora) e qual área foi mais afetada.

## Regras de alerta

| Parâmetro | NORMAL (0 pts) | ATENÇÃO (1 pt) | CRÍTICO (2 pts) |
| :--- | :--- | :--- | :--- |
| Temperatura | 18°C a 30°C | < 18°C ou 31°C a 35°C | > 35°C |
| Comunicação | ≥ 60% | 30% a 59% | < 30% |
| Bateria | ≥ 50% | 20% a 49% | < 20% |
| Oxigênio | ≥ 90% | 80% a 89% | < 80% |
| Estabilidade | ≥ 70% | 40% a 69% | < 40% |

## Classificação do ciclo
- 0 a 2 pontos: MISSÃO ESTÁVEL
- 3 a 5 pontos: MISSÃO EM ATENÇÃO
- 6 a 10 pontos: MISSÃO CRÍTICA
