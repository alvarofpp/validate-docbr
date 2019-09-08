import unittest
import validate_docbr as docbr


class TestCns(unittest.TestCase):
    def setUp(self):
        """ Inicia novo objeto em todo os testes """
        self.cns = docbr.CNS()

    def test_generate(self):
        """ Verifica se o método generate """
        # generate, generate(mask=True)
        cnss = [self.cns.generate() for i in range(10000)]\
                + [self.cns.generate(mask=True) for i in range(10000)]
        self.assertIsInstance(cnss, list)
        self.assertTrue(len(cnss) == 20000)

    def test_generate_list(self):
        """ Verifica se o método generate_list """
        # generate_list
        cnss = self.cns.generate_list(10000)\
                + self.cns.generate_list(10000, True)\
                + self.cns.generate_list(10000, True, True)
        self.assertIsInstance(cnss, list)
        self.assertTrue(len(cnss) == 30000)

    def test_validate(self):
        """ Verifica se o método validate """
        # validate
        for cns in self.cns.generate_list(10000):
            self.assertTrue(self.cns.validate(cns))
