from .BaseDoc import BaseDoc
from random import sample


class CPF(BaseDoc):
    """Classe referente ao Cadastro de Pessoas Físicas (CPF)."""

    def __init__(self):
        self.digits = list(range(10))

    def validate(self, doc):
        """Validar CPF."""

        if len(doc) != 11:
            return False

        return self._check_first_digit(doc) and self._check_second_digit(doc)

    def generate(self):
        """Gerar CPF."""
        # Os nove primeiros dígitos
        cpf = [sample(self.digits, 1)[0] for i in range(9)]

        # Primeiro dígito verificador
        first_digit = 0

        for i in list(range(10, 1, -1)):
            first_digit += int(cpf[10-i]) * i
        first_digit = (first_digit * 10) % 11
        cpf.append(0 if first_digit == 10 else first_digit)

        # Segundo dígito verificador
        second_digit = 0

        for i in list(range(11, 1, -1)):
            second_digit += int(cpf[11-i]) * i
        second_digit = (second_digit * 10) % 11
        cpf.append(0 if second_digit == 10 else second_digit)

        return "".join(str(digit) for digit in cpf)

    def _check_first_digit(self, doc):
        """Validar o primeiro dígito verificador do CPF."""
        sum = 0

        for i in list(range(10, 1, -1)):
            sum += int(doc[10-i]) * i

        sum = (sum * 10) % 11

        if sum == 10:
            sum = 0

        return str(sum) == doc[9]

    def _check_second_digit(self, doc):
        """Validar o segundo dígito verificador do CPF."""
        sum = 0

        for i in list(range(11, 1, -1)):
            sum += int(doc[11-i]) * i

        sum = (sum * 10) % 11

        if sum == 10:
            sum = 0

        return str(sum) == doc[10]
