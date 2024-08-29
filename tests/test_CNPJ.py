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

    def test_mask_on_already_masked_cnpj(self):
        """Verifica se o método mask funciona corretamente."""
        masked_cnpj = self.cnpj.mask('11.222.333/4444-55')
        self.assertEqual(masked_cnpj, '11.222.333/4444-55')

    def test_special_case(self):
        """Verifica os casos especiais de CNPJ."""
        cases = [
            ('00000-000/0000', False),
            ('AAAA0AAAAAAA2AAAAAA', False),
            ('74600269000145', True),
        ]
        for cnpj, is_valid in cases:
            self.assertEqual(self.cnpj.validate(cnpj), is_valid)

    def test_validate_success(self):
        """Testar o método validate do CNPJ."""
        # GIVEN
        doc = '74600269000145'

        # WHEN
        validate_return = self.cnpj.validate(doc)

        # THEN
        self.assertTrue(validate_return)

    def test_validate_wrong_input(self):
        """Testar o método validate do CNPJ em caso de input errado."""
        # GIVEN
        doc = '74600269000145_'

        # WHEN
        validate_return = self.cnpj.validate(doc)

        # THEN
        self.assertFalse(validate_return)

    def test_validate_wrong_length(self):
        """Testar o método validate do CNPJ em caso de tamanho inválido."""
        # GIVEN
        doc = '746002690001450'

        # WHEN
        validate_return = self.cnpj.validate(doc)

        # THEN
        self.assertFalse(validate_return)
