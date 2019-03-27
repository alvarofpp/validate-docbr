files_test = [
    't_CNPJ', 't_CNS', 't_CPF',
]

for filename in files_test:
    exec(open("./{}.py".format(filename)).read())
    print("{} executado com sucesso!".format(filename))
