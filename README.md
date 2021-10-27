# validate-docbr
<a href="https://pypi.org/project/validate-docbr/">
  <img src="https://img.shields.io/pypi/v/validate-docbr.svg" alt="latest release" />
</a>

Pacote Python para validação de documentos brasileiros.

Para instalar o pacote:
```bash
pip install validate-docbr
```

A documentação pode ser acessada [clicando aqui](https://alvarofpp.github.io/validate-docbr).

## Testes
Para realizar os testes basta executar o seguinte comando:

```shell
coverage run -m unittest discover tests && coverage report -m
```

## Documentos
Documentos que estão no pacote:

- [CPF](validate_docbr/CPF.py): Cadastro de Pessoas Físicas;
- [CNH](validate_docbr/CNH.py): Carteira Nacional de Habilitação;
- [CNPJ](validate_docbr/CNPJ.py): Cadastro Nacional da Pessoa Jurídica;
- [CNS](validate_docbr/CNS.py): Cartão Nacional de Saúde;
- [PIS](validate_docbr/PIS.py): PIS/NIS/PASEP/NIT;
- [Título eleitoral](validate_docbr/TituloEleitoral.py): Cadastro que permite cidadãos brasileiros votar;
- [RENAVAM](validate_docbr/RENAVAM.py): Registro Nacional de Veículos Automotores.

Para entender melhor os documentos e suas respectivas classes, basta acessar a [Wiki do projeto](https://github.com/alvarofpp/validate-docbr/wiki).

## Métodos
Todos os documentos possuem os mesmos métodos e funcionam da mesma forma.

### validate
Valida o documento passado como argumento. Retorna um `bool`, `True` caso seja válido, `False` caso contrário . Recebe os parâmetros:

| Parâmetro | Tipo | Valor padrão | Obrigatório | Descrição |
| --------- | ---- | ----------- | ------------ | --------- |
| `doc` | `str`| `''` | X | O documento que se quer validar. |

```python
from validate_docbr import CPF

cpf = CPF()

# Validar CPF
cpf.validate("012.345.678-90")  # True
cpf.validate("012.345.678-91")  # False
```

[Caso especial de CPF](https://alvarofpp.github.io/validate-docbr/guia-de-uso/#caso-especial-de-cpf).

### validate_list

Valida uma lista de documentos passado como argumento. Retorna uma lista de `bool`, `True` caso seja válido, `False` caso contrário. Recebe os parâmetros:

| Parâmetro | Tipo | Valor padrão | Obrigatório | Descrição |
| --------- | ---- | ----------- | ------------ | --------- |
| `docs` | `List[str]`| `[]` | X | A lista de documentos para validar. |

```python
from validate_docbr import CPF

cpf = CPF()

# Validar CPFs
cpf.validate_list(["012.345.678-90", "012.345.678-91"])  # [True, False]
```

### validate_docs
**Observação**: diferente dos outros métodos, esse método é do escopo global do pacote, não precisa-se instanciar uma classe para uso.

Valida vários documentos difererentes. Retorna uma lista com valores `bool` para cada tupla da lista (na mesma ordem), `True` caso seja válido, `False` caso contrário . Recebe os parâmetros:

| Parâmetro | Tipo | Valor padrão | Obrigatório | Descrição |
| --------- | ---- | ----------- | ------------ | --------- |
| `documents` | `List[Tuple[BaseDoc, str]]`| `[]` | X | Lista de tuplas, cada tupla possui como primeiro elemento o tipo de documento e o segundo elemento o valor que se deseja validar. |

```python
import validate_docbr as docbr


# Validar diferentes documentos
docs = [(docbr.CPF, '90396100457'), (docbr.CNPJ, '49910753848365')]
docbr.validate_docs(docs)  # [True, False]
```

### generate
Gera um novo documento, retorna em formato de `str`. Recebe os parâmetros:

| Parâmetro | Tipo | Valor padrão | Obrigatório | Descrição |
| --------- | ---- | ----------- | ------------ | --------- |
| `mask` | `bool` | `False` | - | Quando possui o valor `True`, o documento retornado estará formatado. |

```python
from validate_docbr import CPF

cpf = CPF()

# Gerar novo CPF
new_cpf_one = cpf.generate()  # "01234567890"
new_cpf_two = cpf.generate(mask=True)  # "012.345.678-90"
```

### generate_list
Gera uma lista de documentos, retorna em formato de `list` com elementos do tipo `str`. Recebe os parâmetros:

| Parâmetro | Tipo | Valor padrão | Obrigatório | Descrição |
| --------- | ---- | ----------- | ------------ | --------- |
| `n` | `int` | `1` | X | A quantidade desejada de documentos que serão gerados. |
| `mask` | `bool` | `False` | - | Se os documentos gerados deverão ter ou não máscara. |
| `repeat` | `bool` | `False` | - | Se aceita ou não documentos repetidos. |
    
```python
from validate_docbr import CPF

cpf = CPF()

# Gerar lista de CPFs
cpfs_one = cpf.generate_list(2)  # [ "85215667438", "28293145811" ]
cpfs_two = cpf.generate_list(2, mask=True)  # [ "852.156.674-38", "282.931.458-11" ]
```

### mask
Mascara o documento passado como argumento. Retorna um `str` que é o documento mascarado . Recebe os parâmetros:

| Parâmetro | Tipo | Valor padrão | Obrigatório | Descrição |
| --------- | ---- | ----------- | ------------ | --------- |
| `doc` | `str`| `''` | X | O documento que se quer mascarar. |

```python
from validate_docbr import CPF

cpf = CPF()

cpf_me = "01234567890"

# Mascara o CPF
cpf.mask(cpf_me)  # "012.345.678-90"
```
