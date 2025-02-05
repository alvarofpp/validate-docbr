import unittest

import validate_docbr as docbr


class TestCns(unittest.TestCase):
    """Testa a classe CNS."""

    def setUp(self):
        self.cns = docbr.CNS()

    def test_generate_list_with_validate_list(self):
        # Given
        number_of_documents = 5000
        number_of_documents_expected = number_of_documents * 3

        # When
        cnss = self.cns.generate_list(number_of_documents) \
               + self.cns.generate_list(number_of_documents, mask=True) \
               + self.cns.generate_list(number_of_documents, mask=True, repeat=True)
        validated_cnss = self.cns.validate_list(cnss)

        # Then
        self.assertIsInstance(cnss, list)
        self.assertTrue(len(cnss) == number_of_documents_expected)
        self.assertTrue(sum(validated_cnss) == number_of_documents_expected)

    def test_mask(self):
        # Given
        doc = '111222233334444'
        doc_expected = '111 2222 3333 4444'

        # When
        masked_cns = self.cns.mask(doc)

        # Then
        self.assertEqual(masked_cns, doc_expected)

    def test_special_case(self):
        # Given
        cases = [
            ('AAAAAAAAAAA', False),
            ('', False),
        ]

        # When
        for cns, is_valid in cases:
            doc_validated = self.cns.validate(cns)

            # Then
            self.assertEqual(doc_validated, is_valid)
