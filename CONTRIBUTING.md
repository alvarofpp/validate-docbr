# Contribuindo

Para contribuir com o pacote com a inserção de um novo documento:

- Crie uma _issue_ dizendo sobre o documento que deseja inserir ao pacote;
  - Preferencialmente coloque links que ajudem a entender o algoritmo de geração e validação do documento.
- Realize os procedimentos padrões, sendo que na hora de criar a sua _branch_, referencie a sua _issue_;
- Realize o _pull request_ para a branch _master_.

## Sobre o código

Para novos documentos:

- Criar uma classe com as siglas do documento (herdando a classe pai `BaseDoc`);
- Importar a classe no `__init__.py`;
- Criar testes em `test/`.
