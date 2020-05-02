import unittest
import validate_docbr as docbr


class TestPis(unittest.TestCase):
    """Testar a classe PIS/NIS/PASEP/NIT."""

    def setUp(self):
        """Inicia novo objeto em todo os testes."""
        self.pis = docbr.PIS()

    def test_generate_validate(self):
        """Verifica os métodos de geração e validação de documento."""
        # generate_list
        piss = self.pis.generate_list(5000)\
                + self.pis.generate_list(5000, mask=True)\
                + self.pis.generate_list(5000, mask=True, repeat=True)
        self.assertIsInstance(piss, list)
        self.assertTrue(len(piss) == 15000)

        # validate_list
        piss_validates = self.pis.validate_list(piss)
        self.assertTrue(sum(piss_validates) == 15000)

    def test_mask(self):
        """Verifica se o método mask funciona corretamente."""
        masked_pis = self.pis.mask('23992734770')
        self.assertEqual(masked_pis, '239.92734.77-0')

        masked_pis = self.pis.mask('93999998770')
        self.assertEqual(masked_pis, '939.99998.77-0')
        
        masked_pis = self.pis.mask('03953333770')
        self.assertEqual(masked_pis, '039.53333.77-0')
