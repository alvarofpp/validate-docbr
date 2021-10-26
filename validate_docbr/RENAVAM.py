from .BaseDoc import BaseDoc
from random import sample
from typing import Union


class RENAVAM(BaseDoc):
    """Classe referente ao Registro Nacional de Veículos Automotores (RENAVAM)."""

    def __init__(self):
        self.digits = list(range(10))

    def validate(self, doc: str = '') -> bool:
        """Validar RENAVAM."""
        if not self._validate_input(doc, [' ']):
            return False

        doc = self._only_digits(doc)

        if len(doc) != 11:
            return False

        last_digit = self._generate_last_digit(doc)

        return last_digit == doc[10]

    def generate(self, mask: bool = False) -> str:
        """Gerar Renavam."""
        renavam = [str(sample(self.digits, 1)[0]) for i in range(10)]
        renavam.append(self._generate_last_digit(renavam))

        renavam = ''.join(renavam)
        return renavam

    def mask(self, doc: str = '') -> str:
        """Coloca a máscara de Renavam na variável doc."""
        return "{}-{}".format(doc[:10], doc[10])

    def _generate_last_digit(self, doc: Union[str, list]) -> str:
        """Gerar o dígito verificador do Renavam."""
        sequence = '3298765432'
        sum = 0

        for i in range(0, 10):
            sum += int(doc[i]) * int(sequence[i])

        rest = (sum * 10) % 11

        if rest == 10:
            rest = 0
        return str(rest)
