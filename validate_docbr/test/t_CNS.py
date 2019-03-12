from validate_docbr import CNS

cns = CNS()

cnss = [cns.generate() for i in range(10000)]

for i in cnss:
    assert cns.validate(i)
