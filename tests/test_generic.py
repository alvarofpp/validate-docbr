import unittest
import random

import validate_docbr as docbr


def get_random_number_str(length):
    numbers = '0123456789'
    return ''.join(random.choice(numbers) for i in range(length))


class TestValidateDocs(unittest.TestCase):
    """Testa a função validate_docs"""

    def test_correct_argument(self):
        """Testa a função quando os argumentos estão corretos"""
        DocClasses = [
            docbr.CPF,
            docbr.CNH,
            docbr.CNPJ,
            docbr.CNS,
            docbr.PIS,
            docbr.TituloEleitoral,
        ]

        documents = []
        right_answers = []

        for DocClass in DocClasses:
            # Documentos válidos
            tuples = [(DocClass, doc) for doc in DocClass().generate_list(200)]
            documents += tuples
            right_answers += [True] * len(tuples)

            # Documentos aleatórios
            len_doc = len(DocClass().generate())
            for i in range(200):
                random_doc = get_random_number_str(len_doc)
                documents += [(DocClass, random_doc)]
                right_answers += [DocClass().validate(random_doc)]

        self.assertEqual(docbr.validate_docs(documents), right_answers)

    def test_incorrect_argument(self):
        """Test a função quando os argumentos estão incorretos"""
        with self.assertRaises(TypeError):
            docbr.validate_docs([('cpf', docbr.CPF().generate())])
