import unittest
import validate_docbr as docbr


class TestCpf(unittest.TestCase):
    def setUp(self):
        """ Inicia novo objeto em todo os testes """
        self.cpf = docbr.CPF()

    def test_generate(self):
        """ Verifica se o método generate """
        # generate, generate(mask=True)
        cpfs = [self.cpf.generate() for i in range(10000)]\
                + [self.cpf.generate(mask=True) for i in range(10000)]
        self.assertIsInstance(cpfs, list)
        self.assertTrue(len(cpfs) == 20000)

    def test_generate_list(self):
        """ Verifica se o método generate_list """
        # generate_list
        cpfs = self.cpf.generate_list(10000)\
                + self.cpf.generate_list(10000, True)\
                + self.cpf.generate_list(10000, True, True)
        self.assertIsInstance(cpfs, list)
        self.assertTrue(len(cpfs) == 30000)

    def test_validate(self):
        """ Verifica se o método validate """
        # validate
        for cpf in self.cpf.generate_list(10000):
            self.assertTrue(self.cpf.validate(cpf))

    def test_special_case(self):
        """ Verifica os casos especiais de CPF """
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
        # Entrada consideradas invalidas
        for cpf in cpfs_repeated_digits:
            self.assertFalse(self.cpf.validate(cpf))
        # Entrada consideradas validas
        self.cpf.repeated_digits = True
        for cpf in cpfs_repeated_digits:
            self.assertTrue(self.cpf.validate(cpf))
