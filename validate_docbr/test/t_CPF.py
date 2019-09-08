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

cpf_me = "01234567890"
assert cpf.mask(cpf_me) == "012.345.678-90"

cpf.repeated_digits = False
cpfs_repeated_digits = [
    '000.000.000-00',
    '111.111.111-11',
    '222.222.222-22',
    '333.333.333-33',
    '444.444.444-44',
    '555.555.555-55',
    '666.666.666-66',
    '777.777.777-77',
    '888.888.888-88',
    '999.999.999-99',
]
for cpf_rd in cpfs_repeated_digits:
    assert (cpf.validate(cpf_rd) == False)
