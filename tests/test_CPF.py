import unittest

import validate_docbr as docbr


class TestCpf(unittest.TestCase):
    """Testar a classe CPF."""

    def setUp(self):
        """Inicia novo objeto em todo os testes."""
        self.cpf = docbr.CPF()

    def test_generate_validate(self):
        """Verifica os métodos de geração e validação de documento."""
        # generate_list
        cpfs = self.cpf.generate_list(5000) \
               + self.cpf.generate_list(5000, mask=True) \
               + self.cpf.generate_list(5000, mask=True, repeat=True)
        self.assertIsInstance(cpfs, list)
        self.assertTrue(len(cpfs) == 15000)

        # validate_list
        cpfs_validates = self.cpf.validate_list(cpfs)
        self.assertTrue(sum(cpfs_validates) == 15000)

    def test_mask(self):
        """Verifica se o método mask funciona corretamente."""
        masked_cpf = self.cpf.mask('11122233344')
        self.assertEqual(masked_cpf, '111.222.333-44')

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

        cases = [
            ('AAA.AAA.AAA+AA', False),
            ('04255791000144', False),
        ]
        for cpf, is_valid in cases:
            self.assertEqual(self.cpf.validate(cpf), is_valid)

    def test_add_leading_zeros(self):
        """Verifica se o método de adicionar zeros à esquerda funciona corretamente."""
        cases = [
            ('123456789', '00123456789'),  # 9 digits
            ('12345678901', '12345678901'),  # 11 digits
            ('1234567', '00001234567'),  # 7 digits
        ]
        for cpf_input, expected_output in cases:
            self.assertEqual(self.cpf._complete_with_zeros(cpf_input), expected_output)
        
        # Test if the input is already correct length, it should not add zeros
        self.assertEqual(self.cpf._complete_with_zeros('00123456789'), '00123456789')
        self.assertEqual(self.cpf._complete_with_zeros('23456789012'), '23456789012')