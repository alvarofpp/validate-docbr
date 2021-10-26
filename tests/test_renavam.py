import unittest
import validate_docbr as docbr


class TestRenavam(unittest.TestCase):
    """Testar a classe RENAVAM."""

    def setUp(self):
        """Inicia novo objeto em todo os testes."""
        self.renavam = docbr.RENAVAM()

    def test_generate_validate(self):
        """Verifica os métodos de geração e validação de documento."""
        # generate_list
        renavams = (
                self.renavam.generate_list(1)
                + self.renavam.generate_list(1, mask=True)
                + self.renavam.generate_list(1, mask=True, repeat=True)
        )
        self.assertIsInstance(renavams, list)
        self.assertTrue(len(renavams) == 3)

        # validate_list
        renavams_validates = self.renavam.validate_list(renavams)
        self.assertTrue(sum(renavams_validates) == 3)

    def test_mask(self):
        """Verifica se o método mask funciona corretamente."""
        masked_renavam = self.renavam.mask('13824652268')
        self.assertEqual(masked_renavam, '1382465226-8')

    def test_special_case(self):
        """ Verifica os casos especiais de RENAVAM """
        cases = [
            ('3467875434578764345789654', False),
            ('', False),
            ('AAAAAAAAAAA', False),
            ('38872054170', False),
            ('40999838209', False),
            ('31789431480', False),
            ('38919643060', False),
            ('13824652268', True),
            ('08543317523', True),
            ('09769017014', True),
            ('01993520012', True),
            ('04598137389', True),
            ('05204907510', True),
        ]
        for renavam, is_valid in cases:
            self.assertEqual(self.renavam.validate(renavam), is_valid)
