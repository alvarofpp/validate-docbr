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
