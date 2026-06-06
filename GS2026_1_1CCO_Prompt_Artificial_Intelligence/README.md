# Mission Control AI - AstroData GS-2026

**Integrantes:**
* João Vitor Belchior Domingos Leite - RM: 572478
* Gabriel Pedro de Souza - RM: 572478

## Descrição do Projeto
Sistema de monitoramento de missão espacial para a Global Solution 2026.1 de Ciência da Computação, desenvolvido com uma arquitetura baseada em microsserviços. 

Em vez de utilizarmos o ambiente padrão do Google Colab, construímos uma infraestrutura própria: o sistema utiliza um fluxo no **n8n** (com scripts JavaScript) para gerar dados de telemetria simulados e injetá-los em um banco de dados **PostgreSQL**. A interface web consome esses dados via webhook e os envia para o modelo de IA **Gemma (2B)**, hospedado localmente via **Ollama** em uma VPS. Através de um prompt de sistema embarcado contendo regras operacionais de classificação, o assistente "AstroData" processa a telemetria e gera alertas críticos automatizados em tempo real.

## Demonstração (Evidências do Sistema)

Abaixo estão os registros do funcionamento real da nossa arquitetura integrada:

### 1. Interface Web e Análise da IA
 Interface e IA
![img_2.png](img_2.png)
*Painel web consumindo a telemetria recém-gerada e o retorno da IA estruturando o diagnóstico com base nas regras operacionais.*

### 2. Automação de Geração de Dados (n8n)
 Fluxo n8n
![img.png](img.png)
*Fluxo construído no n8n que atua como backend, gerando os valores dos sensores do foguete e roteando via webhook para armazenamento.*

### 3. Histórico de Telemetria (PostgreSQL)
 [Banco de Dados]
![img_3.png](img_3.png)
*Registros em tempo real da telemetria armazenados no nosso banco de dados, garantindo rastreabilidade das condições da missão.*

## Tecnologias Utilizadas
* **Frontend:** HTML, CSS, JavaScript. 
* **Backend/Orquestração:** N8N
* **Banco de Dados:** PostgreSQL.
* **Inteligência Artificial:** Modelo Gemma (2 bilhões de parâmetros) via Ollama.
* **Infraestrutura:** Servidor VPS próprio hospedando os serviços e a página web. 

## Como Executar

O projeto está totalmente hospedado e funcional na nossa VPS, dispensando a instalação de pacotes locais ou a execução via Colab. Para testar o sistema:

🔗 **[Acessar o Mission Control AI - AstroData](http://srv1596774.hstgr.cloud:8080/chat.html)**

1. Ao abrir o painel, clique no botão **"Atualizar dados"**. Isso acionará nosso webhook no n8n para buscar a telemetria mais recente no banco de dados.
2. Com os dados carregados na tela, o botão **"Analisar com IA"** aparecerá.
3. Clique em "Analisar com IA" para submeter a carga de dados via API ao nosso modelo Gemma na VPS.
4. A IA retornará um relatório situacional do foguete, apontando se os status estão em nível Normal, Atenção ou Crítico.

## Vídeo de Demonstração
[Assistir à apresentação da arquitetura e funcionamento do projeto](https://youtu.be/EbjRTUfPaxk)