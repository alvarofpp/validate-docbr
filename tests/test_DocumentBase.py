import unittest

import validate_docbr as docbr


class DocumentBaseFaker(docbr.DocumentBase):
    def validate(self, doc: str = '') -> bool:
        pass

    def generate(self, mask: bool = False) -> str:
        return "test"

    def mask(self, doc: str = '') -> str:
        pass


class TestDocumentBase(unittest.TestCase):
    """Testa a classe DocumentBase."""

    def setUp(self):
        self.document_base_faker = DocumentBaseFaker()

    def test_generate_list_empty(self):
        # Given
        number_of_documents = 0
        number_of_documents_expected = 0

        # When
        docs = self.document_base_faker.generate_list(number_of_documents)

        # Then
        self.assertIsInstance(docs, list)
        self.assertTrue(len(docs) == number_of_documents_expected)

    def test_validate_input(self):
        # Given
        input_value = "1234567890"
        validated_input_value_expected = True

        # When
        validated_input_value = self.document_base_faker._validate_input(input_value)

        # Then
        self.assertIsInstance(validated_input_value, bool)
        self.assertTrue(validated_input_value == validated_input_value_expected)
