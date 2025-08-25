# Flix API

Flix API é uma aplicação backend desenvolvida em Python utilizando Django e Django REST Framework. Ela fornece endpoints para gerenciamento de dados de filmes, atores e autenticação de usuários, incluindo suporte a autenticação JWT (JSON Web Token).

## Principais Funcionalidades

- **Gerenciamento de Filmes e Atores:** Endpoints para CRUD de filmes e atores.
- **Autenticação JWT:** Utiliza o pacote `rest_framework_simplejwt` para autenticação segura via tokens.
- **Documentação Interativa:** Inclui documentação automática dos endpoints via CoreAPI/OpenAPI, acessível pela interface web.
- **Internacionalização:** Suporte a múltiplos idiomas, incluindo português do Brasil e português europeu, com arquivos `.po` para traduções.
- **Administração:** Interface administrativa do Django para gerenciamento dos dados.

## Estrutura do Projeto

- `actors.csv`: Base de dados inicial de atores.
- `rest_framework/`: Pacote do Django REST Framework, incluindo templates, renderers, schemas e arquivos estáticos.
- `rest_framework_simplejwt/`: Pacote para autenticação JWT.
- `django/contrib/admindocs/locale/`, `django/contrib/admin/locale/`, `django/contrib/auth/locale/`: Arquivos de tradução para internacionalização.
- `Lib/site-packages/`: Dependências Python instaladas.

## Documentação da API

A documentação interativa pode ser acessada via navegador, utilizando os templates em `rest_framework/templates/rest_framework/docs/`. Exemplos de uso em Shell, Python e JavaScript estão disponíveis.

## Autenticação

A autenticação é realizada via JWT, utilizando endpoints fornecidos pelo pacote `rest_framework_simplejwt`. Os tokens podem ser obtidos e renovados conforme a configuração padrão do pacote.

## Internacionalização

O projeto inclui arquivos `.po` para tradução das mensagens do sistema, permitindo fácil adaptação para diferentes idiomas.

## Como Executar

1. Instale as dependências do projeto (Django, djangorestframework, djangorestframework_simplejwt).
2. Realize as migrações do banco de dados.
3. Inicie o servidor de desenvolvimento do Django.
4. Acesse a interface administrativa ou a documentação da API via navegador.

## Exemplos de Uso

- **Requisição via Shell:**
  ```bash
  coreapi get http://localhost:8000/api/
  ```
- **Requisição via Python:**
  ```python
  import coreapi
  client = coreapi.Client()
  schema = client.get("http://localhost:8000/api/")
  ```
- **Requisição via JavaScript:**
  ```javascript
  var client = new coreapi.Client();
  client.action(schema, ["filmes", "list"]).then(function(result) {
      console.log(result);
  });
  ```

## Licença

Este projeto utiliza licenças compatíveis com Django e Django REST Framework.

## Contribuição

Contribuições são bem-vindas! Siga as boas práticas de desenvolvimento e abra um pull request.

