import unittest

import validate_docbr as docbr


class TestRenavam(unittest.TestCase):
    """Testa a classe RENAVAM."""

    def setUp(self):
        self.renavam = docbr.RENAVAM()

    def test_generate_list_with_validate_list(self):
        # Given
        number_of_documents = 10
        number_of_documents_expected = number_of_documents * 2

        # When
        renavams = (
                self.renavam.generate_list(number_of_documents)
                + self.renavam.generate_list(number_of_documents, mask=True)
        )
        validated_renavams = self.renavam.validate_list(renavams)

        # Then
        self.assertIsInstance(renavams, list)
        self.assertTrue(len(renavams) == number_of_documents_expected)
        self.assertTrue(sum(validated_renavams) == number_of_documents_expected)

    def test_mask(self):
        # Given
        doc = '13824652268'
        doc_expected = '1382465226-8'

        # When
        masked_renavam = self.renavam.mask(doc)

        # Then
        self.assertEqual(masked_renavam, doc_expected)

    def test_special_case(self):
        # Given
        cases = [
            ('3467875434578764345789654', False),
            ('', False),
            ('AAAAAAAAAAA', False),
            ('38872054170', False),
            ('40999838209', False),
            ('31789431480', False),
            ('38919643060', False),
            ('13824652268', True),
            ('08543317523', True),
            ('09769017014', True),
            ('01993520012', True),
            ('04598137389', True),
            ('05204907510', True),
        ]

        # When
        for renavam, is_valid in cases:
            doc_validated = self.renavam.validate(renavam)

            # Then
            self.assertEqual(doc_validated, is_valid)
