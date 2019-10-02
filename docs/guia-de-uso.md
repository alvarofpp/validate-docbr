# Métodos
Todos os documentos possuem os mesmos métodos e funcionam da mesma forma.

------------
## validate
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

### Caso especial de CPF
Os CPFs de 000.000.000-00 até 999.999.999-99 são considerados como válidos pois, em alguns casos, existem pessoas vinculadas a eles. Usei a base de dados da [Coleção de CNPJs e CPFs brasileiros do Brasil.IO](https://brasil.io/dataset/documentos-brasil/documents) para verificar esses documentos:

| CPF | Pessoa | Consulta |
| --- | ------ | -------- |
| 000.000.000-00 | - | `https://brasil.io/dataset/documentos-brasil/documents?search=00000000000&document_type=CPF&document=&name=&sources=` |
| 111.111.111-11 | AKA CENTRAL PARK - NEW YORK | `https://brasil.io/dataset/documentos-brasil/documents?search=11111111111&document_type=CPF&document=&name=&sources=` |
| 222.222.222-22 | - | `https://brasil.io/dataset/documentos-brasil/documents?search=22222222222&document_type=CPF&document=&name=&sources=` |
| 333.333.333-33 | - | `https://brasil.io/dataset/documentos-brasil/documents?search=33333333333&document_type=CPF&document=&name=&sources=` |
| 444.444.444-44 | - | `https://brasil.io/dataset/documentos-brasil/documents?search=44444444444&document_type=CPF&document=&name=&sources=` |
| 555.555.555-55 | ISAEL HERMINIO DA SILVA | `https://brasil.io/dataset/documentos-brasil/documents?search=55555555555&document_type=CPF&document=&name=&sources=` |
| 666.666.666-66 | - | `https://brasil.io/dataset/documentos-brasil/documents?search=66666666666&document_type=CPF&document=&name=&sources=` |
| 777.777.777-77 | ANTONIO GONÇALO DA SILVA | `https://brasil.io/dataset/documentos-brasil/documents?search=77777777777&document_type=CPF&document=&name=&sources=` |
| 888.888.888-88 | - | `https://brasil.io/dataset/documentos-brasil/documents?search=88888888888&document_type=CPF&document=&name=&sources=` |
| 999.999.999-99 | JOAQUIM ROCHA MATOS | `https://brasil.io/dataset/documentos-brasil/documents?search=99999999999&document_type=CPF&document=&name=&sources=` |

Porém, é comum optar por não validar esses CPFs. Para isso basta usar o parâmetro `repeated_digits` (por padrão é `False`) da classe `CPF` ou mudar a variável de mesmo nome no objeto criado.
```python
from validate_docbr import CPF

cpf = CPF(repeated_digits=True)

# Validar CPF
cpf.validate("111.111.111-11")  # True

# Não aceitando entradas de 000.000.000-00 até 999.999.999-99
cpf.repeated_digits = False

# Validar CPF
cpf.validate("111.111.111-11")  # False
```

------------
## validate_list

Valida uma lista contendo documentos passado como argumento. Retorna uma lista contendo `bool`, `True` caso seja válido, `False` caso contrário. Recebe os parâmetros:

| Parâmetro | Tipo | Valor padrão | Obrigatório | Descrição |
| --------- | ---- | ----------- | ------------ | --------- |
| `doc` | `List[str]`| `[]` | X | A lista contendo documentos para validar. |

```python
from validate_docbr import CPF

cpf = CPF()

# Validar CPFs
cpf.validate_list(["012.345.678-90", "012.345.678-91"])  # [True, False]
```

------------
## generate
Gera um novo documento, retorna em formato de `str`. Recebe os parâmetros:

| Parâmetro | Tipo | Valor padrão | Obrigatório | Descrição |
| --------- | ---- | ----------- | ------------ | --------- |
| `mask` | `bool` | `False` | - | Quando possui o valor `True`, o documento retornado estará formatado. |

```python
from validate_docbr import CPF

cpf = CPF()

# Gerar novo CPF
new_cpf_one = cpf.generate()  # "01234567890"
new_cpf_two = cpf.generate(True)  # "012.345.678-90"
```

------------
## generate_list
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
cpfs_two = cpf.generate_list(2, True)  # [ "852.156.674-38", "282.931.458-11" ]
```

------------
## mask
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
