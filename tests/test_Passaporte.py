import unittest

import validate_docbr as docbr


class TestPassaporte(unittest.TestCase):
    """Testa a classe Passaporte."""

    def setUp(self):
        self.passaporte = docbr.Passaporte()

    def test_generate_list_with_validate_list(self):
        # Given
        number_of_documents = 10
        number_of_documents_expected = number_of_documents * 2

        # When
        passports = (
                self.passaporte.generate_list(number_of_documents)
                + self.passaporte.generate_list(number_of_documents, mask=True)
        )
        validated_passports = self.passaporte.validate_list(passports)

        # Then
        self.assertIsInstance(passports, list)
        self.assertEqual(len(passports), number_of_documents_expected)
        self.assertEqual(sum(validated_passports), number_of_documents_expected)

    def test_mask(self):
        # Given
        doc = 'AB1234567'
        doc_expected = 'AB-1234567'

        # When
        masked_passport = self.passaporte.mask(doc)

        # Then
        self.assertEqual(masked_passport, doc_expected)

    def test_special_case(self):
        # Given
        cases = [
            ('', False),
            ('000000000', False),
            ('AB123456', False),
            ('AB12345678', False),
            ('AB-1234567', True),
            ('ab1234567', True),
            ('CD 7654321', True),
            ('AB1234-567', True),
        ]

        # When
        for passport, is_valid in cases:
            passport_validated = self.passaporte.validate(passport)

            # Then
            self.assertEqual(passport_validated, is_valid)
