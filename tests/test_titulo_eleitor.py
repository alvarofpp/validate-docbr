import unittest
import validate_docbr as docbr


class TestTituloEleitoral(unittest.TestCase):
    def setUp(self):
        """ Inicia novo objeto em todo os testes """
        self.titulo_eleitoral = docbr.TituloEleitoral()

    def test_generate(self):
        """ Verifica se o método generate """
        # generate, generate(mask=True)
        titulos = [self.titulo_eleitoral.generate() for i in range(10000)] \
                  + [self.titulo_eleitoral.generate(mask=True) for i in range(10000)]
        self.assertIsInstance(titulos, list)
        self.assertTrue(len(titulos) == 20000)

    def test_generate_list(self):
        """ Verifica se o método generate_list """
        # generate_list
        titulo_eleitoral = self.titulo_eleitoral.generate_list(10000) \
                           + self.titulo_eleitoral.generate_list(10000, True) \
                           + self.titulo_eleitoral.generate_list(10000, True, True)
        self.assertIsInstance(titulo_eleitoral, list)
        self.assertTrue(len(titulo_eleitoral) == 30000)

    def test_validate(self):
        """ Verifica se o método validate """
        # validate
        for titulo in self.titulo_eleitoral.generate_list(10000):
            self.assertTrue(self.titulo_eleitoral.validate(titulo))

    def test_mask_returns_correctly_formatted_string(self):
        masked_titulo = self.titulo_eleitoral.mask('123123123123')

        self.assertEqual(masked_titulo, '1231 2312 3123')
