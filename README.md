# validate-docbr
Pacote Python para validar documentos brasileiros.

## Documentos
Documentos que estão no pacote:

- [CPF](https://github.com/alvarofpp/validate-docbr/wiki/CPF)

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