import unittest

import validate_docbr as docbr


class TestCertidao(unittest.TestCase):
    """Testa a classe Certidao."""

    def setUp(self):
        self.certidao = docbr.Certidao()

    def test_generate_list_with_validate_list(self):
        # Given
        number_of_documents = 5000
        number_of_documents_expected = number_of_documents * 2

        # When
        certidoes = self.certidao.generate_list(number_of_documents) \
                    + self.certidao.generate_list(number_of_documents, mask=True)
        validated_certidoes = self.certidao.validate_list(certidoes)

        # Then
        self.assertIsInstance(certidoes, list)
        self.assertTrue(len(certidoes) == number_of_documents_expected)
        self.assertTrue(sum(validated_certidoes) == number_of_documents_expected)

    def test_mask(self):
        # Given
        doc = '10453901552013100012021000012321'
        doc_expected = '104539.01.55.2013.1.00012.021.0000123-21'

        # When
        masked_certidao = self.certidao.mask(doc)

        # Then
        self.assertEqual(masked_certidao, doc_expected)

    def test_special_case(self):
        # Given
        cases = [
            ('3467875434578764345789654', False),
            ('AAAAAAAAAAA', False),
            ('', False),
            ('27610201552018226521370659786633', True),
            ('27610201552018226521370659786630', False),
        ]

        # When
        for certidao, is_valid in cases:
            doc_validated = self.certidao.validate(certidao)

            # Then
            self.assertEqual(doc_validated, is_valid)
