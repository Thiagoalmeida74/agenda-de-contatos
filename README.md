# 📒 Agenda de Contatos em Python

<details open>
<summary><strong>🎯 Descrição do Projeto</strong></summary>

<br>

A **Agenda de Contatos** é uma aplicação desenvolvida em Python para gerenciar contatos diretamente pelo terminal.

O projeto permite realizar operações de **CRUD**, possibilitando cadastrar, listar, buscar, editar e excluir contatos. As informações são armazenadas em um arquivo **JSON**, permitindo que os dados permaneçam salvos mesmo após o encerramento do programa.

Durante o desenvolvimento, o projeto foi estruturado em módulos separados para praticar conceitos importantes de organização de código, separação de responsabilidades, validação de dados, tratamento de erros e comunicação entre arquivos utilizando `import`.

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
- ✅ Validação de campos obrigatórios
- ✅ Validação de telefone
- ✅ Validação básica de e-mail
- ✅ Validação das opções do menu
- ✅ Padronização de nomes
- ✅ Padronização de e-mails
- ✅ Tratamento de erros ao carregar os dados

</details>

---

<details>
<summary><strong>🗺️ Evolução do Projeto</strong></summary>

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
- Utilização do laço `for`

### ✅ Sprint 3 — Busca de Contatos

- Busca de contatos pelo nome
- Verificação de contatos encontrados

### ✅ Sprint 4 — Edição de Contatos

- Alteração do telefone
- Alteração do e-mail
- Salvamento das alterações

### ✅ Sprint 5 — Exclusão de Contatos

- Remoção de contatos cadastrados
- Atualização dos dados após a exclusão

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
- Limpeza e organização do código

### ✅ Sprint 8 — Validações e Tratamento de Erros

- Criação do arquivo `validacao.py`
- Validação de campos obrigatórios
- Padronização de nomes com `.title()`
- Validação de telefone utilizando `.isdigit()`
- Validação básica de e-mail
- Padronização de e-mails com `.lower()`
- Validação das opções do menu
- Reutilização das validações nas operações do sistema
- Tratamento de `FileNotFoundError`
- Tratamento de `json.JSONDecodeError`
- Melhorias na legibilidade e organização do código

🏁 **Projeto concluído após a Sprint 8.**

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
- Validação de dados
- `.strip()`
- `.title()`
- `.lower()`
- `.isdigit()`
- Tratamento de exceções
- `try` e `except`
- `FileNotFoundError`
- `JSONDecodeError`
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
├── main.py
├── funcoes_contatos.py
├── validacao.py
├── persistencia.py
├── contatos.json
├── .gitignore
├── README.md
└── LICENSE
```

### 📄 `main.py`

Responsável pelo funcionamento principal do programa.

- Carrega os contatos
- Exibe o menu
- Recebe as opções do usuário
- Direciona cada opção para sua respectiva funcionalidade

### 📄 `funcoes_contatos.py`

Contém as funções responsáveis pelo gerenciamento dos contatos.

- Adicionar contato
- Listar contatos
- Buscar contato
- Editar contato
- Excluir contato

### 📄 `validacao.py`

Responsável pelas validações dos dados informados pelo usuário.

- Validação de campos vazios
- Validação de telefone
- Validação básica de e-mail
- Validação das opções do menu

### 📄 `persistencia.py`

Responsável pela persistência dos dados.

- Salva os contatos no arquivo JSON
- Carrega os contatos ao iniciar o programa
- Trata erros relacionados ao arquivo e ao JSON

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

## 🏁 Status do Projeto

**Projeto concluído.**

A Agenda de Contatos foi desenvolvida como parte dos estudos em Python e teve como objetivo praticar fundamentos da programação, CRUD, persistência de dados, organização de código, validações e tratamento de erros.

O próximo passo da jornada será um novo projeto com desafios e conceitos mais avançados.

---

## 👨‍💻 Autor

Desenvolvido por **Thiago Almeida** durante sua jornada de estudos em **Desenvolvimento Backend com Python**.