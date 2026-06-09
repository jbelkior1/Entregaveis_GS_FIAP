# Monitoramento de Missão Espacial

**Global Solution 2026.1 - Data Structure and Algorithms**

## Equipe AstroTeam (Dupla)
- João Vitor Belchior Domingos Leite - RM: 572478
- Gabriel Pedro de Souza - RM: 571995

## Sobre o projeto
Sistema feito em JavaScript que roda direto no navegador a partir de um arquivo HTML. O usuário digita temperatura, energia e o status da comunicação da nave, e o sistema avisa se a missão está NORMAL, em ATENÇÃO ou CRÍTICA. Tudo que é registrado fica salvo num histórico até o sistema ser encerrado.

## Como executar
Abrir o arquivo `Sistema_Acomp_Foguete.html` no navegador (duplo clique).

## Menu do sistema
- **Inserir dados** — pega os valores digitados, faz a análise e salva no histórico
- **Visualizar status** — mostra a última leitura com o status atual
- **Executar análise** — lista os alertas da última leitura
- **Histórico das leituras** — mostra todas as leituras já registradas
- **Encerrar sistema** — apaga o histórico

## Regras de verificação automática

| Condição | Alerta gerado | Status |
| :--- | :--- | :--- |
| Temperatura > 80 | Alerta de superaquecimento | CRÍTICO |
| Energia < 20 | Economia de energia | ATENÇÃO |
| Comunicação = 0 | Falha de comunicação | CRÍTICO |
| Nenhuma das anteriores | Tudo normal | NORMAL |

Se a leitura tem qualquer alerta CRÍTICO, o status fica CRÍTICO. Se tem só ATENÇÃO, o status é ATENÇÃO. Sem nenhum alerta, é NORMAL.

## Estruturas de dados usadas
- **Vetor `historico`** — guarda todas as leituras feitas. Cada leitura é um objeto com temperatura, energia, comunicação, lista de alertas e status.
- **Vetor `alertas`** — montado a cada análise. Recebe um item para cada condição que disparou.

## Estruturas de controle
- **Condicionais (`if` / `else`)** — usadas na validação dos campos e nas regras de verificação dos sensores.
- **Laços de repetição (`for`)** — usados para percorrer o vetor de alertas (na análise) e o vetor de histórico (na listagem).
- **Funções** — cada parte do sistema fica em uma função separada para organizar o código.

## Funções do sistema
- `analisarDados(temperatura, energia, comunicacao)` — aplica as condições e devolve o vetor de alertas.
- `definirStatus(alertas)` — recebe os alertas e devolve NORMAL, ATENÇÃO ou CRÍTICO.
- `inserirDados()` — valida os campos do formulário e adiciona a leitura ao histórico.
- `visualizarStatus()` — mostra a última leitura.
- `executarAnalise()` — lista os alertas da última leitura.
- `mostrarHistorico()` — percorre o vetor de histórico e mostra todas as leituras.
- `encerrarSistema()` — limpa o vetor de histórico.

## Fluxograma
O fluxograma do sistema está no arquivo `fluxograma.svg`.

## Vídeo de demonstração
_link a adicionar_
