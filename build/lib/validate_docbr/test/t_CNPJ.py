from validate_docbr import CNPJ

cnpj = CNPJ()

cnpjs = [cnpj.generate() for i in range(10000)]

for i in cnpjs:
    assert cnpj.validate(i)
