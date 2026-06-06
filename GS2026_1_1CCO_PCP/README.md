# Mission Control AI - Missão Astro 

**Global Solution 2026.1 - Pensamento Computacional e Automação com Python**

Este repositório contém o sistema **Mission Control AI**, desenvolvido para simular o monitoramento inteligente de uma missão espacial experimental. O sistema organiza dados simulados, analisa as informações automaticamente em diferentes ciclos e apresenta um relatório final detalhado sobre a situação operacional da operação.

##  Equipe AstroTeam
* **João Vitor Belchior** - RM: 572478
* **Gabriel Pedro de Souza** - RM: 571995

##  Sobre o Projeto
Durante a simulação, o sistema avalia 5 áreas vitais da missão:
1. Temperatura interna
2. Comunicação com a base
3. Sistema de energia
4. Suporte de oxigênio
5. Estabilidade operacional

A cada ciclo de monitoramento, o programa analisa a telemetria, emite um nível de risco para cada área, classifica o estado geral do ciclo e recomenda ações automáticas para o controle da missão. Ao final, um relatório completo é gerado no terminal apontando tendências de melhora ou piora e indicando o sistema que mais sofreu degradação.

## Regras de Alerta e Sistema de Risco
A inteligência lógica de decisão para os alertas segue a tabela base do projeto. Cada classificação gera uma pontuação de risco para o ciclo: **NORMAL (0 pontos)**, **ATENÇÃO (1 ponto)** e **CRÍTICO (2 pontos)**.

| Parâmetro monitorado | NORMAL (0 pts) | ATENÇÃO (1 pt) | CRÍTICO (2 pts) |
| :--- | :--- | :--- | :--- |
| **Temperatura** | 18°C a 30°C | < 18°C ou 31°C a 35°C | > 35°C |
| **Comunicação** | ≥ 60% | 30% a 59% | < 30% |
| **Bateria** | ≥ 50% | 20% a 49% | < 20% |
| **Oxigênio** | ≥ 90% | 80% a 89% | < 80% |
| **Estabilidade** | ≥ 70% | 40% a 69% | < 40% |

**Classificação do Ciclo (Soma da Pontuação):**
* **0 a 2 pontos:** MISSÃO ESTÁVEL
* **3 a 5 pontos:** MISSÃO EM ATENÇÃO
* **6 a 10 pontos:** MISSÃO CRÍTICA


