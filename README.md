# 📒 Agenda de Contatos em Python

<details open>
<summary><strong>🎯 Descrição do Projeto</strong></summary>

<br>

A **Agenda de Contatos** é uma aplicação desenvolvida em Python para gerenciar contatos diretamente pelo terminal.

O projeto permite realizar operações de **CRUD**, possibilitando cadastrar, listar, buscar, editar e excluir contatos. As informações são armazenadas em um arquivo **JSON**, permitindo que os dados permaneçam salvos mesmo após o encerramento do programa.

Além das funcionalidades principais, o projeto foi estruturado em módulos separados para praticar conceitos importantes de organização de código, separação de responsabilidades e comunicação entre arquivos utilizando `import`.

</details>

---

<details>
<summary><strong>📋 Funcionalidades</strong></summary>

<br>

- ✅ Cadastro de contatos
- ✅ Listagem de contatos
- ✅ Busca de contatos pelo nome
- ✅ Edição de telefone e e-mail
- ✅ Exclusão de contatos
- ✅ Persistência dos dados em arquivo JSON
- ✅ Carregamento automático dos contatos ao iniciar o programa

</details>

---

<details>
<summary><strong>🗺️ Roadmap e Evolução do Projeto</strong></summary>

<br>

### ✅ Sprint 0 — Estrutura do Projeto

- Criação do repositório
- Configuração do Git
- Criação do README
- Adição da licença
- Estrutura inicial do projeto

### ✅ Sprint 1 — Cadastro de Contatos

- Criação do menu principal
- Cadastro de contatos
- Utilização de dicionários para armazenar os dados

### ✅ Sprint 2 — Listagem de Contatos

- Listagem de todos os contatos cadastrados
- Introdução ao laço `for`

### ✅ Sprint 3 — Busca de Contatos

- Busca de contatos pelo nome

### ✅ Sprint 4 — Edição de Contatos

- Alteração do telefone
- Alteração do e-mail

### ✅ Sprint 5 — Exclusão de Contatos

- Remoção de contatos cadastrados

### ✅ Sprint 6 — Persistência de Dados

- Salvamento dos contatos em arquivo JSON
- Carregamento automático dos contatos ao iniciar o programa

### ✅ Sprint 7 — Refatoração e Organização

- Separação do código em módulos
- Criação do arquivo `funcoes_contatos.py`
- Criação do arquivo `persistencia.py`
- Utilização de `import`
- Utilização de parâmetros entre funções
- Utilização de `return`
- Separação de responsabilidades
- Organização do `.gitignore`
- Limpeza e comentários no código

</details>

---

<details>
<summary><strong>🧠 Conceitos Praticados</strong></summary>

<br>

Durante o desenvolvimento deste projeto foram praticados conceitos como:

- Funções
- Parâmetros de funções
- Retorno de valores com `return`
- Estruturas condicionais (`if`, `elif` e `else`)
- Estruturas de repetição (`while`)
- Laço `for`
- Listas
- Dicionários
- CRUD
- Manipulação de arquivos
- JSON
- Módulos em Python
- Importação de funções
- Separação de responsabilidades
- Organização de código
- Versionamento com Git
- GitHub

</details>

---

<details>
<summary><strong>🛠️ Tecnologias Utilizadas</strong></summary>

<br>

- 🐍 Python 3
- 📄 JSON
- 🌳 Git
- ☁️ GitHub

</details>

---

<details>
<summary><strong>🗂️ Estrutura do Projeto</strong></summary>

<br>

```text
agenda-de-contatos/
│
├── funcoes_contatos.py
├── persistencia.py
├── main.py
├── contatos.json
├── .gitignore
├── README.md
└── LICENSE
```

### 📄 `main.py`

Responsável por controlar o funcionamento principal do programa.

- Carrega os contatos
- Exibe o menu
- Recebe as opções do usuário
- Chama as funções responsáveis por cada operação

### 📄 `funcoes_contatos.py`

Contém as funções responsáveis pelo gerenciamento dos contatos.

- Adicionar contato
- Listar contatos
- Buscar contato
- Editar contato
- Excluir contato

### 📄 `persistencia.py`

Responsável pela persistência dos dados.

- Salva os contatos no arquivo JSON
- Carrega os contatos ao iniciar o programa

### 📄 `contatos.json`

Arquivo utilizado para armazenar os contatos cadastrados.

</details>

---

<details>
<summary><strong>▶️ Como Executar</strong></summary>

<br>

Clone o repositório:

```bash
git clone https://github.com/Thiagoalmeida74/agenda-de-contatos.git
```

Entre na pasta do projeto:

```bash
cd agenda-de-contatos
```

Execute o programa:

```bash
python main.py
```

</details>

---

<details>
<summary><strong>🚀 Próximos Passos</strong></summary>

<br>

O projeto continuará sendo evoluído conforme o avanço nos estudos de Python e Desenvolvimento Backend.

Possíveis melhorias futuras:

- Validação dos dados cadastrados
- Melhorias na busca de contatos
- Tratamento de erros
- Busca sem diferenciação entre maiúsculas e minúsculas
- Melhor organização e evolução da estrutura do projeto
- Interface gráfica ou API no futuro

</details>

---

## 👨‍💻 Autor

Desenvolvido por **Thiago Almeida** durante sua jornada de estudos em **Desenvolvimento Backend com Python**.