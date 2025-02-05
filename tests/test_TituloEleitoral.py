import unittest

import validate_docbr as docbr


class TestTituloEleitoral(unittest.TestCase):
    def setUp(self):
        self.titulo_eleitoral = docbr.TituloEleitoral()

    def test_generate_list_with_validate_list(self):
        # Given
        number_of_documents = 5000
        number_of_documents_expected = number_of_documents * 3

        # When
        titulos_eleitorais = self.titulo_eleitoral.generate_list(number_of_documents) \
                           + self.titulo_eleitoral.generate_list(
                                number_of_documents,
                                True
                            ) \
                           + self.titulo_eleitoral.generate_list(
                                number_of_documents,
                                True,
                                True
                            )
        validated_titulos_eleitorais = self.titulo_eleitoral.validate_list(
            titulos_eleitorais
        )

        # Then
        self.assertIsInstance(titulos_eleitorais, list)
        self.assertTrue(len(titulos_eleitorais) == number_of_documents_expected)
        self.assertTrue(
            sum(validated_titulos_eleitorais) == number_of_documents_expected
        )

    def test_mask(self):
        # Given
        doc = '123123123123'
        doc_expected = '1231 2312 3123'

        # When
        masked_titulo = self.titulo_eleitoral.mask(doc)

        # Then
        self.assertEqual(masked_titulo, doc_expected)

    def test_special_case(self):
        # Given
        cases = [
            ('3467875434578764345789654', False),
            ('AAAAAAAAAAA', False),
            ('', False),
        ]

        # When
        for titulo_eleitoral, is_valid in cases:
            doc_validated = self.titulo_eleitoral.validate(titulo_eleitoral)

            # Then
            self.assertEqual(doc_validated, is_valid)
