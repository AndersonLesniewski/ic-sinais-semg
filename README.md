# 🧠 IC - Sinais Biomédicos para Interfaces Homem-Máquina

Projeto de **Iniciação Científica** desenvolvido por  
**Anderson Rafael da Silva Lesniewski**  
sob orientação do **Dr. Fabio Luiz Bertotti**  
📍 **Universidade Tecnológica Federal do Paraná (UTFPR) – Câmpus Pato Branco**  
📅 *Início: Outubro de 2025*

---

## 🎯 Objetivo Geral

O projeto tem como objetivo estudar e desenvolver técnicas de **processamento de sinais biomédicos** aplicadas ao controle de **interfaces homem-máquina (IHM)**, com ênfase em aplicações médicas, tecnologias assistivas e próteses controladas.

A pesquisa envolve o uso de sinais **eletromiográficos (sEMG)**, explorando métodos de **filtragem, análise espectral e aprendizado de máquina (Machine Learning)** para identificar padrões musculares e permitir o controle inteligente de dispositivos.

---

## 🧩 Estrutura do Projeto

IC - Sinais sEMG/
├── artigos/ # Artigos e referências científicas
├── data/ # Bases de dados (.mat, .csv, etc.)
├── notebooks/ # Notebooks Jupyter
├── src/ # Scripts auxiliares e funções
├── .gitignore # Arquivos e pastas ignoradas pelo Git
├── requirements.txt # Dependências do projeto
└── README.md # Este documento

---

## ⚙️ Como executar o projeto

1. **Clone o repositório**
   ```bash
   git clone https://github.com/AndersonLesniewski/ic-sinais-semg.git
   cd ic-sinais-semg

2. **Crie um ambiente virtual (opcional)**
    python -m venv .venv
    .venv\Scripts\activate   # Windows
    source .venv/bin/activate   # Linux/Mac

3. **Instale as dependências**
    pip install -r requirements.txt

4. **Execute os notebooks**
    jupyter notebook

## 🧪 Organização por etapas

Os experimentos e relatórios da Iniciação Científica são organizados em notebooks quinzenais, nomeados conforme o período:

| Notebook              | Período     | Descrição resumida                                                       |
| --------------------- | ----------- | ------------------------------------------------------------------------ |
| `Semanas_01_02.ipynb` | Semanas 1–2 | Sinais simulados, fundamentos de processamento sEMG                      |
| `Semanas_03_04.ipynb` | Semanas 3–4 | Processamento de sinais reais (NinaPro DB1 – filtragem e FFT)            |
| *(futuros)*           | ...         | Extração de *features*, aprendizado de máquina, controle de dispositivos |

## 📚 Referências

NinaPro Database 1 – Non-Invasive Adaptive Prosthetics
https://ninapro.hevs.ch/instructions/DB1.html

Atzori, M., et al. (2014). Electromyography data for non-invasive naturally-controlled robotic hand prostheses. Scientific Data, 1:140053.

De Luca, C. J. (2006). Electromyography. Encyclopedia of Medical Devices and Instrumentation.

## 👨‍🔬 Autor
Anderson Rafael da Silva Lesniewski
📍 Universidade Tecnológica Federal do Paraná (UTFPR) – Câmpus Pato Branco
💻 https://github.com/AndersonLesniewski