# >> Django resumo interativo

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092e20.svg?style=for-the-badge&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)

## > Sobre o Projeto
Este projeto transforma meu currículo em uma aplicação web dinâmica utilizando o framework **Django**. A ideia foi sair do PDF básico e demonstrar, na prática, como estruturar um ambiente web real, lidando com backend, organização de arquivos e navegação inteligente.

## > Tecnologias e Conceitos Aplicados
Para construir esse sistema, utilizei os pilares fundamentais do desenvolvimento web com Django:

* **Django Routing System:** Configuração completa de URLs e rotas para navegar entre Home, Habilidades e Pretensões sem arquivos perdidos.
* **Django Templates:** Uso de herança de templates e tags de bloco para manter o código limpo (DRY) e eficiente.
* **Web Design com Flexbox:** Estruturação de menus e botões interativos para uma experiência de usuário moderna.
* **Ambiente Isolado (venv):** Gestão de dependências e ambiente de desenvolvimento Python.

## > Estrutura de Navegação
O projeto foi separado de forma organizada para facilitar a manutenção:
* `home.html` -> Página de boas-vindas.
* `habilidades.html` -> Exibição técnica de skills.
* `pretencao.html` -> Objetivos profissionais.

## > Como rodar na sua máquina
```bash
# 1. Clone o repositório
git clone [https://github.com/felipecanazza3-dev/curriculo-django.git](https://github.com/felipecanazza3-dev/curriculo-django.git)

# 2. Crie e ative a venv
python -m venv .venv
.\.venv\Scripts\activate

# 3. Instale o Django
pip install django

# 4. Inicie o servidor
python manage.py runserver
