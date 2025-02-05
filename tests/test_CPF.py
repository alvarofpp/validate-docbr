import unittest

import validate_docbr as docbr


class TestCpf(unittest.TestCase):
    """Testa a classe CPF."""

    def setUp(self):
        self.cpf = docbr.CPF()

    def test_generate_list_with_validate_list(self):
        # Given
        number_of_documents = 5000
        number_of_documents_expected = number_of_documents * 3

        # When
        cpfs = self.cpf.generate_list(number_of_documents) \
               + self.cpf.generate_list(number_of_documents, mask=True) \
               + self.cpf.generate_list(number_of_documents, mask=True, repeat=True)
        validated_cpfs = self.cpf.validate_list(cpfs)

        # Then
        self.assertIsInstance(cpfs, list)
        self.assertTrue(len(cpfs) == number_of_documents_expected)
        self.assertTrue(sum(validated_cpfs) == number_of_documents_expected)

    def test_mask(self):
        # Given
        doc = '11122233344'
        doc_expected = '111.222.333-44'

        # When
        masked_cpf = self.cpf.mask(doc)

        # Then
        self.assertEqual(masked_cpf, doc_expected)

    def test_special_case(self):
        # Given
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
        cases = [
            ('AAA.AAA.AAA+AA', False),
            ('04255791000144', False),
        ]

        # When
        for cpf in cpfs_repeated_digits:
            doc_validated = self.cpf.validate(cpf)

            # Then
            self.assertFalse(doc_validated)

        # When
        self.cpf.repeated_digits = True
        for cpf in cpfs_repeated_digits:
            doc_validated = self.cpf.validate(cpf)

            # Then
            self.assertTrue(doc_validated)

        # When
        for cpf, is_valid in cases:
            doc_validated = self.cpf.validate(cpf)

            # Then
            self.assertEqual(doc_validated, is_valid)

    def test_add_leading_zeros(self):
        # Given
        cases = [
            ('123456789', False),
            ('12345678901', False),
            ('1234567', False),
            ('9380826044', True)
        ]

        # When
        for cpf, is_valid in cases:
            doc_validated = self.cpf.validate(cpf)

            # Then
            self.assertEqual(doc_validated, is_valid)
