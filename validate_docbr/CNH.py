from .BaseDoc import BaseDoc
from random import sample
from typing import Union


class CNH(BaseDoc):
    """Classe referente ao Carteira Nacional de Habilitação (CNH)."""

    def __init__(self):
        self.digits = list(range(10))

    def validate(self, doc: str = '') -> bool:
        """Validar CNH."""
        if not self._validate_input(doc, [' ']):
            return False

        doc = self._only_digits(doc)

        if len(doc) != 11 or self._is_repeated_digits(doc):
            return False

        first_digit = self._generate_first_digit(doc)
        second_digit = self._generate_second_digit(doc)

        return first_digit == doc[9] and second_digit == doc[10]

    def generate(self, mask: bool = False) -> str:
        """Gerar CNH."""
        cnh = [str(sample(self.digits, 1)[0]) for i in range(9)]
        cnh.append(self._generate_first_digit(cnh))
        cnh.append(self._generate_second_digit(cnh))

        cnh = ''.join(cnh)
        return self.mask(cnh) if mask else cnh

    def mask(self, doc: str = '') -> str:
        """Coloca a máscara de CNH na variável doc."""
        return "{} {} {} {}".format(doc[:3], doc[3:6], doc[6:9], doc[9:])

    def _generate_first_digit(self, doc: Union[str, list]) -> str:
        """Gerar o primeiro dígito verificador da CNH."""
        self.dsc = 0
        sum = 0

        for i in range(9, 0, -1):
            sum += int(doc[9 - i]) * i

        first_value = sum % 11
        if first_value >= 10:
            first_value, self.dsc = 0, 2
        return str(first_value)

    def _generate_second_digit(self, doc: Union[str, list]) -> str:
        """Gerar o segundo dígito verificador da CNH."""
        sum = 0

        for i in range(1, 10):
            sum += int(doc[i-1]) * i

        rest = sum % 11

        second_value = rest - self.dsc
        if second_value < 0:
            second_value += 11
        if second_value >= 10:
            second_value = 0
        return str(second_value)

    def _is_repeated_digits(self, doc: str) -> bool:
        """Verifica se é uma CNH contém com números repetidos.
        Exemplo: 11111111111"""
        return len(set(doc)) == 1
