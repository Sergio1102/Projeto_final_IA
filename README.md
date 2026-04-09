# Gerador de Aulas de Robótica (Multi-Agent System)

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![LangGraph](https://img.shields.io/badge/LangGraph-AI_Agents-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red)
![Gemini](https://img.shields.io/badge/Gemini-2.5_Flash-green)

Um sistema multiagente inteligente projetado para auxiliar professores e educadores na criação de planos de aula dinâmicos e práticos focados em **Robótica Educacional**.

Este projeto utiliza **LangGraph** para orquestrar uma equipe de agentes de IA e **Streamlit** para fornecer uma interface web amigável e interativa.

## Sobre o Projeto

O objetivo deste sistema é transformar um simples tema de aula (ex: "Semáforo com Arduino") em um guia completo, estruturado e viável para o ensino médio profissionalizante. O diferencial do projeto é a implementação do conceito de **Human-in-the-Loop**, onde o sistema pausa a geração para receber a aprovação e o feedback crítico do professor antes de finalizar o documento.

## Funcionalidades

- **Orquestração de Agentes:** Três agentes especializados trabalhando em pipeline (Técnico, Pedagógico e Revisor).
- **Human-in-the-Loop:** Pausa programada no fluxo do grafo para avaliação humana.
- **Persistência de Memória:** O sistema lembra do contexto da sessão utilizando `MemorySaver`.
- **Interface Web Interativa:** Construída com Streamlit, com suporte a renderização de Markdown para documentos polidos.

## Arquitetura dos Agentes

O fluxo do sistema (Grafo) é dividido em três "cérebros":

1. **Agente Técnico:** Analisa o tema, sugere componentes viáveis (ex: Arduino, materiais recicláveis) e cria o passo a passo da montagem física.
2. **Agente Pedagógico:** Transforma a proposta técnica em uma aula dinâmica (Problematização, Mão na Massa e Fechamento).
3. **Avaliação Humana (Pausa):** O fluxo é interrompido. O usuário lê o esboço e insere suas exigências/correções.
4. **Agente Revisor:** Aplica rigorosamente o feedback humano e formata o guia final da aula.

## Como Executar o Projeto

Siga os passos abaixo para rodar o projeto localmente na sua máquina.

### Pré-requisitos
- Python 3.10 ou superior instalado.
- Chave de API do [Google AI Studio](https://aistudio.google.com/).

### Instalação

1. Clone o repositório:
```bash
git clone [https://github.com/Sergio1102/Projeto_final_IA.git](https://github.com/Sergio1102/Projeto_final_IA.git)
cd Projeto_final_IA
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv meu_ambiente
source meu_ambiente/bin/activate  # Linux/Mac
# ou meu_ambiente\Scripts\activate no Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
   
Crie um arquivo chamado .env na raiz do projeto e adicione sua chave de API do Google:
```
GOOGLE_API_KEY=sua_chave_de_api_aqui
```

### Executando a Aplicação Web
Com o ambiente ativado e o .env configurado, inicie o servidor do Streamlit:
```bash
streamlit run app.py
```
O projeto abrirá automaticamente no seu navegador no endereço `http://localhost:8501`.

## Estrutura do Projeto
```
├── core/
│   ├── __init__.py       # Transforma a pasta em um pacote Python
│   ├── agentes.py        # Prompts, integração com LLM e funções dos agentes
│   └── estado.py         # Tipagem e definição do estado do LangGraph
├── .env.example          # Molde para as chaves de API
├── .gitignore            # Arquivos ignorados pelo Git
├── app.py                # Interface web e execução do grafo (Streamlit)
├── requirements.txt      # Dependências do projeto
└── README.md             # Documentação
```

## Tecnologias Utilizadas
- LangGraph: Construção do fluxo de estado e agentes.
- LangChain: Integração com o LLM.
- Streamlit: Criação do frontend em Python.
- Google Generative AI: Modelo Gemini utilizado como cérebro dos agentes.
---
Desenvolvido com Python para fins educacionais e de pesquisa.
