import unittest
import validate_docbr as docbr


class TestCnh(unittest.TestCase):
    """Testar a classe CNH."""

    def setUp(self):
        """Inicia novo objeto em todo os testes."""
        self.cnh = docbr.CNH()

    def test_generate_validate(self):
        """Verifica os métodos de geração e validação de documento."""
        # generate_list
        cnhs = (
            self.cnh.generate_list(1)
            + self.cnh.generate_list(1, mask=True)
            + self.cnh.generate_list(1, mask=True, repeat=True)
        )
        self.assertIsInstance(cnhs, list)
        self.assertTrue(len(cnhs) == 3)

        # validate_list
        cnhs_validates = self.cnh.validate_list(cnhs)
        self.assertTrue(sum(cnhs_validates) == 3)

    def test_mask(self):
        """Verifica se o método mask funciona corretamente."""
        masked_cpf = self.cnh.mask('11122233344')
        self.assertEqual(masked_cpf, '111 222 333 44')

    def test_special_case(self):
        """ Verifica os casos especiais de CNH """
        cases = [
            ('00000000000', False),
            ('78623161668', False),
            ('0123 456 789 10', False),
            ('65821310502', True),
            ('658 213 105 02', True),
            ('10764125809', True),
            ('77625261946', True)
        ]
        for cnh, is_valid in cases:
            self.assertEqual(self.cnh.validate(cnh), is_valid)
