from .BaseDoc import BaseDoc
from random import sample


class CPF(BaseDoc):
    """Classe referente ao Cadastro de Pessoas Físicas (CPF)."""

    def __init__(self):
        self.digits = list(range(10))

    def validate(self, doc: str) -> bool:
        """Validar CPF."""
        doc = list(self._only_digits(doc))

        if len(doc) != 11:
            return False

        return self._generate_first_digit(doc) == doc[9]\
               and self._generate_second_digit(doc) == doc[10]

    def generate(self, mask: bool = False) -> str:
        """Gerar CPF."""
        # Os nove primeiros dígitos
        cpf = [str(sample(self.digits, 1)[0]) for i in range(9)]

        # Gerar os dígitos verificadores
        cpf.append(self._generate_first_digit(cpf))
        cpf.append(self._generate_second_digit(cpf))

        cpf = "".join(cpf)
        if mask:
            return "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[-2:])

        return cpf

    def _generate_first_digit(self, doc: list) -> str:
        """Gerar o primeiro dígito verificador do CPF."""
        sum = 0

        for i in range(10, 1, -1):
            sum += int(doc[10 - i]) * i

        sum = (sum * 10) % 11

        if sum == 10:
            sum = 0

        return str(sum)

    def _generate_second_digit(self, doc: list) -> str:
        """Gerar o segundo dígito verificador do CPF."""
        sum = 0

        for i in range(11, 1, -1):
            sum += int(doc[11-i]) * i

        sum = (sum * 10) % 11

        if sum == 10:
            sum = 0

        return str(sum)
