# Global Solution – Sistema de Orientação de Carreiras em Python

**Disciplina:** Pensamento Computacional e Automação com Python   

## Integrantes

- Arthur Marangoni Furlan – RM: 564665  
- Gustavo Sartori S. Grigoletto – RM: 565726  
- Vinicius Macedo Carvalho – RM: 563791  

---

## Descrição do projeto e propósito

Este projeto tem como objetivo desenvolver um sistema simples, em Python orientado a objetos, que auxilie na reflexão sobre carreiras na área de tecnologia.

A aplicação simula uma ferramenta de orientação profissional:

- O usuário informa seu nome.
- Em seguida, avalia seu nível de conhecimento em um conjunto de competências (como lógica de programação, criatividade, colaboração, adaptabilidade, análise de dados, etc.) usando uma escala de 0 a 5.
- O sistema compara esse “perfil” com um conjunto de carreiras pré-definidas na área de tecnologia:
  - Cientista de Dados  
  - Engenheira de IA  
  - UX Designer  
  - Desenvolvedora Full Stack  
  - Analista de Segurança Cibernética  
- Para cada carreira, há um conjunto de competências com pesos diferentes, indicando o quanto cada habilidade é importante para aquela área.
- Com base nesses pesos e nas notas informadas pelo usuário, o sistema calcula uma porcentagem de compatibilidade entre o perfil e cada carreira.
- Ao final, o sistema:
  - exibe todas as carreiras avaliadas com sua respectiva porcentagem de compatibilidade;
  - destaca a(s) carreira(s) com maior compatibilidade;
  - mostra uma mensagem orientando o usuário a pesquisar melhor antes de tomar qualquer decisão.

O foco do projeto é:

- conectar conceitos de **orientação de carreiras** com **lógica de programação**;
- utilizar **classes, objetos e métodos** para estruturar o problema;
- demonstrar o uso de **estruturas de dados (listas, dicionários)** para representar competências e pesos;
- estimular a reflexão sobre o “trabalho do futuro” a partir de habilidades técnicas e comportamentais.

---

## Instruções de execução

### 1. Pré-requisitos

- Python instalado (versão 3.x)

### 2. Estrutura de arquivos

Coloque os três arquivos na mesma pasta:

- `app.py`  
- `perfil.py`  
- `carreira.py`  

Exemplo de estrutura:

```text
projeto_carreiras/
├── app.py
├── perfil.py
└── carreira.py
