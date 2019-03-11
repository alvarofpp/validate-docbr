# validate-docbr
Pacote Python para validação de documentos brasileiros.

## Documentos
Documentos que estão no pacote:

- [CPF](https://github.com/alvarofpp/validate-docbr/wiki/CPF)
- [CNPJ](https://github.com/alvarofpp/validate-docbr/wiki/CNPJ)

Para entender melhor os documentos e suas respectivas classes, basta acessar a parte de Wiki do projeto.

### CPF
Cadastro de Pessoas Físicas.

```python
from validate_docbr import CPF

cpf = CPF()

# Gerar novo CPF
new_cpf = cpf.generate()
# Validar CPF
cpf.validate(new_cpf)

```

### CNPJ
Cadastro de Pessoas Físicas.

```python
from validate_docbr import CNPJ

cnpj = CNPJ()

# Gerar novo CNPJ
new_cnpj = cnpj.generate()
# Validar CNPJ
cnpj.validate(new_cnpj)

```