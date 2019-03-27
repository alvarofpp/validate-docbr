from validate_docbr import CPF

cpf = CPF()

# generate, generate(mask=True)
cpfs = [cpf.generate() for i in range(10000)] + [cpf.generate(mask=True) for i in range(10000)]
# generate_list
cpfs = cpfs + cpf.generate_list(10000)\
        + cpf.generate_list(10000, True)\
        + cpf.generate_list(10000, True, True)

for i in cpfs:
    assert cpf.validate(i)
