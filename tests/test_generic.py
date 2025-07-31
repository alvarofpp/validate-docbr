import random
import unittest

import validate_docbr as docbr


def get_random_number_str(length):
    numbers = '0123456789'
    return ''.join(random.choice(numbers) for _ in range(length))


class TestValidateDocs(unittest.TestCase):
    """Testa a função validate_docs"""

    def test_validate_docs(self):
        # Given
        doc_classes = [
            docbr.CPF,
            docbr.CNH,
            docbr.CNPJ,
            docbr.CNS,
            docbr.PIS,
            docbr.TituloEleitoral,
        ]
        documents = []
        right_answers = []
        number_of_documents = 100
        
        # When
        for doc_class in doc_classes:
            valid_documents = [
                (doc_class, doc)
                for doc in doc_class().generate_list(number_of_documents)
            ]
            documents += valid_documents
            right_answers += [True] * len(valid_documents)

            len_doc = len(doc_class().generate())
            for _ in range(number_of_documents):
                random_doc = get_random_number_str(len_doc)
                documents += [(doc_class, random_doc)]
                right_answers += [doc_class().validate(random_doc)]
                
        # Then
        self.assertEqual(docbr.validate_docs(documents), right_answers)

    def test_validate_docs_type_error(self):
        # Given
        cpf = [('cpf', docbr.CPF().generate())]
        
        # When-Then
        with self.assertRaises(TypeError):
            docbr.validate_docs(cpf)
