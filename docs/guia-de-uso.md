# Guia de uso

Todos os documentos possuem os mesmos métodos e funcionam
da mesma forma.

## validate

Valida o documento passado como argumento. Retorna um `bool`,
`True` caso seja válido, `False` caso contrário.
Recebe os parâmetros:

| Parâmetro | Tipo  | Valor padrão | Obrigatório | Descrição          |
| --------- | ----- | ------------ | ----------- | ------------------ |
| `doc`     | `str` | `''`         | X           | Documento a validar. |

```python
from validate_docbr import CPF

cpf = CPF()

# Validar CPF
cpf.validate("012.345.678-90")  # True
cpf.validate("012.345.678-91")  # False
```

### Caso especial de CPF

Os CPFs de 000.000.000-00 até 999.999.999-99 são
considerados como válidos pois, em alguns casos, existem
pessoas vinculadas a eles. Usei a base de dados da
[Coleção de CNPJs e CPFs brasileiros do Brasil.IO][brasil.io]
para verificar esses documentos:

| CPF | Pessoa |
| --- | ------ |
| 000.000.000-00 | - |
| 111.111.111-11 | AKA CENTRAL PARK - NEW YORK |
| 222.222.222-22 | - |
| 333.333.333-33 | - |
| 444.444.444-44 | - |
| 555.555.555-55 | ISAEL HERMINIO DA SILVA |
| 666.666.666-66 | - |
| 777.777.777-77 | ANTONIO GONÇALO DA SILVA |
| 888.888.888-88 | - |
| 999.999.999-99 | JOAQUIM ROCHA MATOS |

Porém, é comum optar por não validar esses CPFs. Para isso
basta usar o parâmetro `repeated_digits` (por padrão é
`False`) da classe `CPF` ou mudar a variável de mesmo nome
no objeto criado.

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

## validate_list

Valida uma lista de documentos passado como argumento.
Retorna uma lista de `bool`, `True` caso seja válido,
`False` caso contrário. Recebe os parâmetros:

| Parâmetro | Tipo         | Valor padrão | Obrigatório | Descrição       |
| --------- | ------------ | ------------ | ----------- | --------------- |
| `docs`    | `list[str]`  | `[]`         | X           | Lista de docs.  |

```python
from validate_docbr import CPF

cpf = CPF()

# Validar CPFs
cpf.validate_list(["012.345.678-90", "012.345.678-91"])
# [True, False]
```

## validate_docs

**Observação**: diferente dos outros métodos, esse método é
do escopo global do pacote, não precisa-se instanciar uma
classe para uso.

Valida vários documentos diferentes. Retorna uma lista com
valores `bool` para cada tupla da lista (na mesma ordem),
`True` caso seja válido, `False` caso contrário.
Recebe os parâmetros:

| Parâmetro   | Tipo                | Obrigatório | Descrição       |
| ----------- | ------------------- | ----------- | --------------- |
| `documents` | `list[tuple[...]]`  | X           | Lista de tuplas.|

Cada tupla possui como primeiro elemento o tipo de documento
(`DocumentBase`) e o segundo o valor que se deseja validar.

```python
import validate_docbr as docbr

# Validar diferentes documentos
docs = [
    (docbr.CPF, '90396100457'),
    (docbr.CNPJ, '49910753848365'),
]
docbr.validate_docs(docs)  # [True, False]
```

## generate

Gera um novo documento, retorna em formato de `str`.
Recebe os parâmetros:

| Parâmetro | Tipo   | Valor padrão | Obrigatório | Descrição        |
| --------- | ------ | ------------ | ----------- | ---------------- |
| `mask`    | `bool` | `False`      | -           | Retorna com máscara. |

```python
from validate_docbr import CPF

cpf = CPF()

# Gerar novo CPF
new_cpf_one = cpf.generate()  # "01234567890"
new_cpf_two = cpf.generate(True)  # "012.345.678-90"
```

## generate_list

Gera uma lista de documentos, retorna em formato de `list`
com elementos do tipo `str`. Recebe os parâmetros:

| Parâmetro | Tipo   | Valor padrão | Obrigatório | Descrição       |
| --------- | ------ | ------------ | ----------- | --------------- |
| `n`       | `int`  | `1`          | X           | Quantidade.     |
| `mask`    | `bool` | `False`      | -           | Com máscara.    |
| `repeat`  | `bool` | `False`      | -           | Aceita repetidos. |

```python
from validate_docbr import CPF

cpf = CPF()

# Gerar lista de CPFs
cpfs_one = cpf.generate_list(2)
# [ "85215667438", "28293145811" ]
cpfs_two = cpf.generate_list(2, True)
# [ "852.156.674-38", "282.931.458-11" ]
```

## mask

Mascara o documento passado como argumento. Retorna um `str`
que é o documento mascarado. Recebe os parâmetros:

| Parâmetro | Tipo  | Valor padrão | Obrigatório | Descrição          |
| --------- | ----- | ------------ | ----------- | ------------------ |
| `doc`     | `str` | `''`         | X           | Documento a mascarar. |

```python
from validate_docbr import CPF

cpf = CPF()

cpf_me = "01234567890"

# Mascara o CPF
cpf.mask(cpf_me)  # "012.345.678-90"
```

[brasil.io]: https://brasil.io/dataset/documentos-brasil/documents
