from validate_docbr import CPF

cpf = CPF()

cpfs = [cpf.generate() for i in range(10000)]

for i in cpfs:
    assert cpf.validate(i)
