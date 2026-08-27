import unittest
from importlib import import_module
from unittest.mock import patch

import validate_docbr as docbr


class TestTituloEleitoral(unittest.TestCase):
    def setUp(self):
        self.titulo_eleitoral = docbr.TituloEleitoral()

    def test_generate_list_with_validate_list(self):
        # Given
        number_of_documents = 10
        number_of_documents_expected = number_of_documents * 2

        # When
        titulos_eleitorais = self.titulo_eleitoral.generate_list(number_of_documents) \
                           + self.titulo_eleitoral.generate_list(
                                number_of_documents,
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

    def test_generate_reaches_all_state_identifiers(self):
        # Given
        expected_state_identifiers = [
            f'{state_identifier:02}' for state_identifier in range(1, 29)
        ]
        state_indexes = iter(range(len(expected_state_identifiers)))

        def deterministic_sample(population, _):
            if population is self.titulo_eleitoral.digits:
                return [population[0]]
            return [population[next(state_indexes)]]

        # When
        titulo_eleitoral_module = import_module('validate_docbr.TituloEleitoral')
        with patch.object(
            titulo_eleitoral_module,
            'sample',
            side_effect=deterministic_sample,
        ):
            generated_state_identifiers = [
                self.titulo_eleitoral.generate()[8:10]
                for _ in expected_state_identifiers
            ]

        # Then
        self.assertEqual(
            generated_state_identifiers,
            expected_state_identifiers,
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
