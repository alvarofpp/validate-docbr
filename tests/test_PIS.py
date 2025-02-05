import unittest

import validate_docbr as docbr


class TestPis(unittest.TestCase):
    """Testa a classe PIS/NIS/PASEP/NIT."""

    def setUp(self):
        self.pis = docbr.PIS()

    def test_generate_list_with_validate_list(self):
        # Given
        number_of_documents = 5000
        number_of_documents_expected = number_of_documents * 3

        # When
        piss = self.pis.generate_list(number_of_documents) \
               + self.pis.generate_list(number_of_documents, mask=True) \
               + self.pis.generate_list(number_of_documents, mask=True, repeat=True)
        validated_piss = self.pis.validate_list(piss)

        # Then
        self.assertIsInstance(piss, list)
        self.assertTrue(len(piss) == number_of_documents_expected)
        self.assertTrue(sum(validated_piss) == number_of_documents_expected)

    def test_mask(self):
        # Given
        doc = '23992734770'
        doc_expected = '239.92734.77-0'

        # When
        masked_pis = self.pis.mask(doc)

        # Then
        self.assertEqual(masked_pis, doc_expected)

    def test_special_case(self):
        # Given
        cases = [
            ('3467875434578764345789654', False),
            ('AAAAAAAAAAA', False),
            ('', False),
        ]

        # When
        for pis, is_valid in cases:
            doc_validated = self.pis.validate(pis)

            # Then
            self.assertEqual(doc_validated, is_valid)
