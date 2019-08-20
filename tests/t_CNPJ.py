from validate_docbr import CNPJ

cnpj = CNPJ()

# generate, generate(mask=True)
cnpjs = [cnpj.generate() for i in range(10000)] + [cnpj.generate(mask=True) for i in range(10000)]
# generate_list
cnpjs = cnpjs + cnpj.generate_list(10000)\
        + cnpj.generate_list(10000, True)\
        + cnpj.generate_list(10000, True, True)

for i in cnpjs:
    assert cnpj.validate(i)
