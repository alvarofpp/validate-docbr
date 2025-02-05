import unittest

import validate_docbr as docbr


class TestCnh(unittest.TestCase):
    """Testa a classe CNH."""

    def setUp(self):
        self.cnh = docbr.CNH()

    def test_generate_list_with_validate_list(self):
        # Given
        number_of_documents = 5000
        number_of_documents_expected = number_of_documents * 3

        # When
        cnhs = (
                self.cnh.generate_list(number_of_documents)
                + self.cnh.generate_list(number_of_documents, mask=True)
                + self.cnh.generate_list(number_of_documents, mask=True, repeat=True)
        )
        validated_cnhs = self.cnh.validate_list(cnhs)

        # Then
        self.assertIsInstance(cnhs, list)
        self.assertTrue(len(cnhs) == number_of_documents_expected)
        self.assertTrue(sum(validated_cnhs) == number_of_documents_expected)

    def test_mask(self):
        # Given
        doc = '11122233344'
        doc_expected = '111 222 333 44'

        # When
        masked_cpf = self.cnh.mask(doc)

        # Then
        self.assertEqual(masked_cpf, doc_expected)

    def test_special_case(self):
        # Given
        cases = [
            ('00000000000', False),
            ('AAAAAAAAAAA', False),
            ('78623161668', False),
            ('0123 456 789 10', False),
            ('65821310502', True),
            ('658 213 105 02', True),
            ('10764125809', True),
            ('77625261946', True)
        ]

        # When
        for cnh, is_valid in cases:
            doc_validated = self.cnh.validate(cnh)

            # Then
            self.assertEqual(doc_validated, is_valid)
