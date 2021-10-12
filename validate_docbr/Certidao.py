from .BaseDoc import BaseDoc
from random import sample


class Certidao(BaseDoc):
    """Classe referente a Certidão de Nascimento/Casamento/Óbito."""

    def __init__(self):
        self.digits = list(range(10))

    def validate(self, doc: str = '') -> bool:
        """Método para validar a Certidão de Nascimento/Casamento/Óbito."""
        if not self._validate_input(doc, ['.', '-']):
            return False

        doc = self._only_digits(doc)

        if len(doc) != 32:
            return False

        num = list(doc[:-2])
        dv = doc[-2:]

        expected_dv = self._generate_verifying_digit(num)

        if dv == expected_dv:
            return True

        return False

    def _weighted_sum(self, value) -> int:
        sum = 0
        multiplier = 32 - len(value)

        for i in range(len(value)):
            sum += int(value[i]) * multiplier

            multiplier += 1
            multiplier = 0 if multiplier > 10 else multiplier

        return sum

    def generate(self, mask: bool = False) -> str:
        """Método para gerar a Certidão de Nascimento/Casamento/Óbito."""
        # Os trinta primeiros dígitos
        certidao = [str(sample(self.digits, 1)[0]) for i in range(30)]

        # Gerar os dígitos verificadores
        certidao.append(self._generate_verifying_digit(certidao))

        certidao = "".join(certidao)

        return self.mask(certidao) if mask else certidao

    def mask(self, doc: str = '') -> str:
        """Mascara para a Certidão de Nascimento/Casamento/Óbito."""
        return "{}.{}.{}.{}.{}.{}.{}.{}-{}".format(
            doc[:6], doc[6:8], doc[8:10], doc[10:14],
            doc[14], doc[15:20], doc[20:23], doc[23:30], doc[-2:])

    def _generate_verifying_digit(self, doc: list) -> str:
        """Gerar o dígito verificador da Certidao."""
        dv1 = self._weighted_sum(doc) % 11
        dv1 = 1 if dv1 > 9 else dv1

        dv2 = self._weighted_sum(doc+[dv1]) % 11
        dv2 = 1 if dv2 > 9 else dv2

        return str(dv1)+str(dv2)
