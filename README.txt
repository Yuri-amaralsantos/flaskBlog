Blog API com Flask, Vue.js e PostgreSQL

Este repositório contém uma aplicação web de blog desenvolvida com Flask para o backend, Vue.js para o frontend e PostgreSQL como banco de dados. O projeto inclui funcionalidades completas de autenticação com JWT, postagem e moderação de conteúdo, e sistema de privilégios para administradores.

Funcionalidades

Autenticação JWT: Registro e login seguro utilizando JSON Web Tokens (JWT).

Postagens: Usuários autenticados podem criar, editar e deletar suas próprias postagens.

Comentários: Comentar postagens e remover próprios comentários.

Moderação: Administradores podem editar e remover qualquer postagem ou comentário.

Banco de Dados: Utiliza PostgreSQL para armazenamento seguro e eficiente dos dados.

Tecnologias Utilizadas

Backend: Flask, Flask-JWT-Extended, Flask-SQLAlchemy, Flask-Migrate

Frontend: Vue.js 3, Vue Router, Axios

Banco de Dados: PostgreSQL

Instalação e Configuração

Backend (Flask)

Clone o repositório e acesse o diretório do projeto:

git clone https://github.com/seu-usuario/nome-do-repo.git
cd nome-do-repo/backend

Crie um ambiente virtual e instale as dependências:

python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt

Configure as variáveis de ambiente no arquivo .env:

FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=sua_chave_secreta
DATABASE_URL=postgresql://usuario:senha@localhost:5432/seu_banco
JWT_SECRET_KEY=sua_chave_jwt

Execute as migrações do banco de dados:

flask db upgrade

Inicie o servidor:

flask run

Frontend (Vue.js)

Acesse o diretório do frontend:

cd ../frontend

Instale as dependências:

npm install

Configure as variáveis de ambiente no arquivo .env:

VITE_API_URL=http://localhost:5000

Inicie o servidor de desenvolvimento:

npm run dev

Uso

Registre um novo usuário ou faça login para acessar as funcionalidades do blog.

Crie, edite e exclua postagens.

Comente nas postagens e gerencie seus comentários.

Se for administrador, modere postagens e comentários.

Contribuição

Fork o repositório.

Crie um branch com a sua feature ou correção de bug: git checkout -b minha-feature

Commit suas mudanças: git commit -m 'Adiciona nova funcionalidade'

Envie para o repositório remoto: git push origin minha-feature

Abra um Pull Request.

Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

