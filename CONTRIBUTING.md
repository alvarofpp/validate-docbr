# Contribuindo
Para contribuir ao pacote:
- Crie uma _issue_ dizendo sobre o documento que deseja inserir ao pacote;
  - Preferencialmente coloque links que ajudem a entender o algoritmo de geração e válidação do documento.
- Realize os procedimentos padrões, sendo que na hora de criar a sua _branch_, referencie a sua _issue_;
- Realize o _pull request_ para a branch _staging_. PRs diretamente para a _master_ serão negados.

# Sobre o código
Para novos documentos:
- Criar uma classe com as siglas do documento (como classe pai a `BaseDoc`);
- Importar a classe no `__init__.py`;
- Criar teste em `test/`.
