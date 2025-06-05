import string
from random import sample
from typing import Union

from .BaseDoc import BaseDoc


class CNPJ(BaseDoc):
    """Classe referente ao Cadastro Nacional da Pessoa Jurídica (CNPJ)."""

    def __init__(self):
        self.digits = list(range(10))
        self.digits_and_letters = list(string.ascii_uppercase) + list(string.digits)
        self.weights_first = list(range(5, 1, -1)) + list(range(9, 1, -1))
        self.weights_second = list(range(6, 1, -1)) + list(range(9, 1, -1))

    def validate(self, doc: str = '') -> bool:
        """Validar CNPJ."""
        if not self._validate_input(doc, ['.', '/', '-'], allow_letters=True):
            return False

        doc = doc.strip().upper()
        doc = self._only_digits_and_letters(doc)

        if len(doc) != 14:
            return False

        return self._generate_first_digit(doc) == doc[12] \
               and self._generate_second_digit(doc) == doc[13]

    def generate(self, mask: bool = False, digits_only: bool = True) -> str:
        """Gerar CNPJ."""
        # Os doze primeiros dígitos
        if digits_only:
            cnpj = [str(sample(self.digits, 1)[0]) for i in range(12)]
        else:
            cnpj = [sample(self.digits_and_letters, 1)[0] for i in range(12)]

        # Gerar os dígitos verificadores
        cnpj.append(self._generate_first_digit(cnpj))
        cnpj.append(self._generate_second_digit(cnpj))

        cnpj = "".join(cnpj)

        return self.mask(cnpj) if mask else cnpj

    def mask(self, doc: str = '') -> str:
        """Coloca a máscara de CNPJ na variável doc."""
        return f"{doc[:2]}.{doc[2:5]}.{doc[5:8]}/{doc[8:12]}-{doc[-2:]}"

    def _generate_first_digit(self, doc: Union[str, list]) -> str:
        """Gerar o primeiro dígito verificador do CNPJ."""
        sum = 0

        for i in range(12):
            sum += (ord(str(doc[i])) - 48) * self.weights_first[i]

        sum = sum % 11
        sum = 0 if sum < 2 else 11 - sum

        return str(sum)

    def _generate_second_digit(self, doc: Union[str, list]) -> str:
        """Gerar o segundo dígito verificador do CNPJ."""
        sum = 0

        for i in range(13):
            sum += (ord(str(doc[i])) - 48) * self.weights_second[i]

        sum = sum % 11
        sum = 0 if sum < 2 else 11 - sum

        return str(sum)
