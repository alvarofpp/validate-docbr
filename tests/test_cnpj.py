import unittest
import validate_docbr as docbr


class TestCnpj(unittest.TestCase):
    def setUp(self):
        """ Inicia novo objeto em todo os testes """
        self.cnpj = docbr.CNPJ()

    def test_generate(self):
        """ Verifica se o método generate """
        # generate, generate(mask=True)
        cnpjs = [self.cnpj.generate() for i in range(10000)]\
                + [self.cnpj.generate(mask=True) for i in range(10000)]
        self.assertIsInstance(cnpjs, list)
        self.assertTrue(len(cnpjs) == 20000)

    def test_generate_list(self):
        """ Verifica se o método generate_list """
        # generate_list
        cnpjs = self.cnpj.generate_list(10000)\
                + self.cnpj.generate_list(10000, True)\
                + self.cnpj.generate_list(10000, True, True)
        self.assertIsInstance(cnpjs, list)
        self.assertTrue(len(cnpjs) == 30000)

    def test_validate(self):
        """ Verifica se o método validate """
        # validate
        for cnpj in self.cnpj.generate_list(10000):
            self.assertTrue(self.cnpj.validate(cnpj))
