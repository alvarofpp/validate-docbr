from validate_docbr import CNS

cns = CNS()

# generate, generate(mask=True)
cnss = [cns.generate() for i in range(10000)] + [cns.generate(mask=True) for i in range(10000)]
# generate_list
cnss = cnss + cns.generate_list(10000)\
        + cns.generate_list(10000, True)\
        + cns.generate_list(10000, True, True)

for i in cnss:
    assert cns.validate(i)
