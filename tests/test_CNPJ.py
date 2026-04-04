import unittest

import validate_docbr as docbr


class TestCnpj(unittest.TestCase):
    """Testa a classe CNPJ."""

    def setUp(self):
        self.cnpj = docbr.CNPJ()

    def test_generate_list_with_validate_list(self):
        # Given
        number_of_documents = 10
        number_of_documents_expected = number_of_documents * 2
        
        # When
        cnpjs = self.cnpj.generate_list(number_of_documents) \
                + self.cnpj.generate_list(number_of_documents, mask=True)
        validated_cnpjs = self.cnpj.validate_list(cnpjs)
        
        # Then
        self.assertIsInstance(cnpjs, list)
        self.assertTrue(len(cnpjs) == number_of_documents_expected)
        self.assertTrue(sum(validated_cnpjs) == number_of_documents_expected)

    def test_mask(self):
        # Given
        doc = '11222333444455'
        doc_expected = '11.222.333/4444-55'
        
        # When
        masked_cnpj = self.cnpj.mask(doc)
        
        # Then
        self.assertEqual(masked_cnpj, doc_expected)

    def test_special_case(self):
        # Given
        cases = [
            ('00000-000/0000', False),
            ('AAAA0AAAAAAA2AAAAAA', False),
            ('74600269000145', True),
        ]

        # When
        for cnpj, is_valid in cases:
            doc_validated = self.cnpj.validate(cnpj)

            # Then
            self.assertEqual(doc_validated, is_valid)

    def test_validate_success(self):
        # Given
        doc = '74600269000145'

        # When
        doc_validated = self.cnpj.validate(doc)

        # Then
        self.assertTrue(doc_validated)

    def test_validate_wrong_input(self):
        # Given
        doc = '74600269000145_'

        # When
        validate_return = self.cnpj.validate(doc)

        # Then
        self.assertFalse(validate_return)

    def test_validate_wrong_length(self):
        # Given
        doc = '746002690001450'

        # When
        validate_return = self.cnpj.validate(doc)

        # Then
        self.assertFalse(validate_return)

    def test_alphanumeric(self):
        # Given
        cases = [
            ('12.aBc.345/01dE-35', True),
            ('12ABC34501DE35', True),
            ('12.ABC.345/01DE-34', False),
        ]

        # When
        for doc, is_valid in cases:
            doc_validated = self.cnpj.validate(doc)

            # Then
            self.assertEqual(doc_validated, is_valid)

    def test_generate_alphanumeric(self):
        # Given
        number_of_documents = 10

        # When
        cnpjs = self.cnpj.generate_list(number_of_documents)
        cnpjs_alpha = [
            self.cnpj.generate(digits_only=False)
            for _ in range(number_of_documents)
        ]
        validated = self.cnpj.validate_list(cnpjs + cnpjs_alpha)

        # Then
        self.assertTrue(all(validated))
