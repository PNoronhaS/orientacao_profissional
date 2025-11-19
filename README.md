# Sistema de Orientação Profissional 🎓

Projeto acadêmico em Python que recomenda carreiras com base nas competências do usuário.  
O sistema coleta informações sobre o perfil do estudante, compara com requisitos de diferentes carreiras e sugere trilhas de aprendizado e tendências futuras.  
Além disso, gera um **relatório em PDF** com todas as recomendações.

## 🚀 Funcionalidades

- Criação e atualização de perfil com competências e níveis (1 a 5).
- Recomendações de carreira com cálculo de compatibilidade.
- Sugestão de trilhas de aprendizado para preencher lacunas.
- Exibição de tendências futuras do mercado de trabalho.
- Geração de relatório em PDF com perfil, recomendações e tendências.

## 📂 Estrutura do Projeto

│ 
├── main.py # Ponto de entrada do sistema 
└── app/ 
├── init.py 
├── cli.py # Menu e interação com usuário 
├── modelos.py # Classes Perfil e Carreira 
├── dados.py # Base de carreiras e competências 
├── servicos.py # Lógica de recomendação e trilhas 
└── persistencia.py # Salvar perfil e gerar relatório em PDF

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- Biblioteca [fpdf](https://pypi.org/project/fpdf/) para geração de PDF

## 📦 Instalação e Uso

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/orientacao_profissional.git
   cd orientacao_profissional
```
2. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/Scripts/activate   # Windows
source venv/bin/activate       # Linux/Mac
```
3. Instale dependências:
```bash
pip install fpdf
```
4. Execute o sistema:
```bash
python main.py
```

---


```markdown
## 📑 Exemplo de Uso
```
**Menu principal:**

===============================
SISTEMA DE ORIENTAÇÃO PROFISSIONAL
===============================

1. Criar/Atualizar meu perfil

2. Ver recomendações de carreira

3. Ver tendências futuras

4. Sair

5. Gerar relatório em PDF


### Relatório em PDF:
Após criar seu perfil e gerar recomendações, escolha a opção **5**.  
Um arquivo `relatorio.pdf` será criado com:
- Nome e competências
- Carreiras recomendadas
- Trilhas de aprendizado
- Tendências futuras

## 🎯 Objetivo Acadêmico

Este projeto foi desenvolvido como trabalho de faculdade para demonstrar:
- Estruturação de código em Python
- Modularização e boas práticas
- Persistência de dados
- Geração de relatórios automatizados
- Aplicação prática em orientação profissional

## 👨‍🏫 Autor

- **Nome:** Pedro Noronha dos Santos
- **Nome:** Lucas Mendes Moraes 
- **Disciplina:** Pensamento Computacional e Automação com Python
- **Professor:** Alexandre Russi Jr.
- **Instituição:** Fiap  
