import unittest
import validate_docbr as docbr


class TestCnpj(unittest.TestCase):
    """Testar a classe CNPJ."""

    def setUp(self):
        """Inicia novo objeto em todo os testes."""
        self.cnpj = docbr.CNPJ()

    def test_generate_validate(self):
        """Verifica os métodos de geração e validação de documento."""
        # generate_list
        cnpjs = self.cnpj.generate_list(5000) \
                + self.cnpj.generate_list(5000, mask=True) \
                + self.cnpj.generate_list(5000, mask=True, repeat=True)
        self.assertIsInstance(cnpjs, list)
        self.assertTrue(len(cnpjs) == 15000)

        # validate_list
        cnpjs_validates = self.cnpj.validate_list(cnpjs)
        self.assertTrue(sum(cnpjs_validates) == 15000)

    def test_mask(self):
        """Verifica se o método mask funciona corretamente."""
        masked_cnpj = self.cnpj.mask('11222333444455')
        self.assertEqual(masked_cnpj, '11.222.333/4444-55')
