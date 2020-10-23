from .BaseDoc import BaseDoc
from random import sample
from typing import List


class TituloEleitoral(BaseDoc):
    """Classe referente ao Título eleitoral"""

    def __init__(self):
        self.digits = list(range(10))
        self.first_check_digit_weights = list(range(2, 10))
        self.second_check_digit_weights = list(range(7, 10))
        self.first_check_digit_doc_slice = slice(0, 8)
        self.second_check_digit_doc_slice = slice(8, 10)

    def validate(self, doc: str = '') -> bool:
        """Método para validar o título eleitoral."""
        if not self._validate_input(doc, [' ']):
            return False

        doc_digits = list(map(int, self._only_digits(doc=doc)))

        if len(doc_digits) != 12:
            return False

        first_check_digit = self._compute_first_check_digit(doc_digits=doc_digits)
        second_check_digit = self._compute_second_check_digit(doc_digits=doc_digits, first_check_digit=first_check_digit)

        return first_check_digit == doc_digits[-2] and second_check_digit == doc_digits[-1]

    def generate(self, mask: bool = False) -> str:
        """Método para gerar um título eleitoral válido."""
        document_digits = [sample(self.digits, 1)[0] for _ in range(8)]

        state_identifier = self._generate_valid_state_identifier()
        document_digits.extend(map(int, state_identifier))

        first_check_digit = self._compute_first_check_digit(doc_digits=document_digits)
        second_check_digit = self._compute_second_check_digit(doc_digits=document_digits,
                                                               first_check_digit=first_check_digit)
        document_digits.extend([first_check_digit, second_check_digit])

        document = ''.join(map(str, document_digits))

        if mask:
            return self.mask(doc=document)

        return document

    def mask(self, doc: str = '') -> str:
        """Mascara o documento enviado"""
        return '{} {} {}'.format(doc[0:4], doc[4:8], doc[8:])

    def _compute_first_check_digit(self, doc_digits: List[int]) -> int:
        """Método que calcula o primeiro dígito verificador."""
        doc_digits_to_consider = doc_digits[self.first_check_digit_doc_slice]
        terms = [
            doc_digit * multiplier
            for doc_digit, multiplier in zip(doc_digits_to_consider, self.first_check_digit_weights)
        ]

        total = sum(terms)

        if total % 11 == 10:
            return 0

        return total % 11

    def _compute_second_check_digit(self, doc_digits: List[int], first_check_digit: int) -> int:
        """Método que calcula o segundo dígito verificador."""
        doc_digits_to_consider = doc_digits[self.second_check_digit_doc_slice] + [first_check_digit]
        terms = [
            doc_digit * multiplier
            for doc_digit, multiplier in zip(doc_digits_to_consider, self.second_check_digit_weights)
        ]

        total = sum(terms)

        if total % 11 == 10:
            return 0

        return total % 11

    def _generate_valid_state_identifier(self) -> str:
        state_identifier = str(sample(range(1, 19), 1)[0])
        return state_identifier.zfill(2)
