import unittest
import validate_docbr as docbr


class TestCns(unittest.TestCase):
    """Testar a classe CNS."""

    def setUp(self):
        """Inicia novo objeto em todo os testes."""
        self.cns = docbr.CNS()

    def test_generate_validate(self):
        """Verifica os métodos de geração e validação de documento."""
        # generate_list
        cnss = self.cns.generate_list(5000) \
               + self.cns.generate_list(5000, mask=True) \
               + self.cns.generate_list(5000, mask=True, repeat=True)
        self.assertIsInstance(cnss, list)
        self.assertTrue(len(cnss) == 15000)

        # validate_list
        cnss_validates = self.cns.validate_list(cnss)
        self.assertTrue(sum(cnss_validates) == 15000)

    def test_mask(self):
        """Verifica se o método mask funciona corretamente."""
        masked_cns = self.cns.mask('111222233334444')
        self.assertEqual(masked_cns, '111 2222 3333 4444')
