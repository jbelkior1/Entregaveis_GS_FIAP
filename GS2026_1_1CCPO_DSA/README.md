# Monitoramento de Missão Espacial

**Global Solution 2026.1 - Data Structure and Algorithms**

## Equipe AstroTeam
- João Vitor Belchior - RM: 572478
- Gabriel Pedro de Souza - RM: 571995

## Sobre o projeto
Sistema feito em JavaScript que roda direto no navegador a partir de um arquivo HTML. O usuário informa temperatura, energia e status da comunicação, e o sistema analisa os dados, emite alertas e mantém um histórico das leituras.

## Como executar
Abrir o arquivo `Sistema_Acomp_Foguete.html` no navegador (duplo clique).

## Menu do sistema
- Inserir dados
- Visualizar status
- Executar análise
- Histórico das leituras
- Encerrar sistema

## Regras de verificação automática

| Condição | Resposta |
| :--- | :--- |
| Temperatura > 80 | Alerta de superaquecimento |
| Energia < 20 | Economia de energia |
| Comunicação = 0 | Falha de comunicação |

## Status operacional
- **CRÍTICO**: superaquecimento ou falha de comunicação
- **ATENÇÃO**: economia de energia
- **NORMAL**: nenhum alerta

## Estruturas usadas
- Vetor `historico` para armazenar todas as leituras
- Vetor `alertas` montado a cada análise
- Condicionais (`if`) para verificar sensores e validar entrada
- Laços `for` para percorrer alertas e histórico
- Funções separadas para cada parte da lógica

## Fluxograma
Disponível no arquivo `fluxograma.svg`.

## Vídeo de demonstração
_link a adicionar_
