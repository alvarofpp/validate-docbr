from random import sample

from validate_docbr.DocumentBase import DocumentBase


class Certidao(DocumentBase):
    """Classe referente à Certidão de Nascimento/Casamento/Óbito."""

    def __init__(self) -> None:
        self.digits = list(range(10))

    def validate(self, doc: str = '') -> bool:
        """Valida a Certidão de Nascimento/Casamento/Óbito.

        Args:
            doc: Certidão a ser validada. Aceita com ou sem máscara.

        Returns:
            True se a Certidão for válida, False caso contrário.
        """
        if not self._validate_input(doc, ['.', '-']):
            return False

        doc = self._only_digits(doc)

        if len(doc) != 32:
            return False

        base_digits = list(doc[:-2])
        check_digits = doc[-2:]
        expected_check_digits = self._generate_check_digits(base_digits)

        return check_digits == expected_check_digits

    def _weighted_sum(self, value: list) -> int:
        """Calcula a soma ponderada dos dígitos com multiplicador cíclico.

        O multiplicador inicia em ``32 - len(value)`` e incrementa a cada
        posição, reiniciando para 0 quando ultrapassa 10.

        Args:
            value: Lista com os dígitos a serem somados.

        Returns:
            Resultado da soma ponderada.
        """
        total = 0
        multiplier = 32 - len(value)

        for digit in value:
            total += int(digit) * multiplier
            multiplier += 1
            if multiplier > 10:
                multiplier = 0

        return total

    def generate(self, mask: bool = False) -> str:
        """Gera uma Certidão de Nascimento/Casamento/Óbito válida.

        Args:
            mask: Se True, retorna a Certidão formatada
                (ex: ``XXXXXX.XX.XX.XXXX.X.XXXXX.XXX.XXXXXXX-XX``).

        Returns:
            Certidão gerada em formato string.
        """
        certidao = [str(sample(self.digits, 1)[0]) for _ in range(30)]

        certidao.append(self._generate_check_digits(certidao))

        certidao = "".join(certidao)

        return self.mask(certidao) if mask else certidao

    def mask(self, doc: str = '') -> str:
        """Coloca a máscara de Certidão no documento.

        Args:
            doc: Certidão sem máscara (32 dígitos).

        Returns:
            Certidão formatada no padrão
            ``XXXXXX.XX.XX.XXXX.X.XXXXX.XXX.XXXXXXX-XX``.
        """
        return "{}.{}.{}.{}.{}.{}.{}.{}-{}".format(
            doc[:6], doc[6:8], doc[8:10], doc[10:14],
            doc[14], doc[15:20], doc[20:23], doc[23:30], doc[-2:])

    def _generate_check_digits(self, doc: list) -> str:
        """Gera os dígitos verificadores da Certidão.

        Args:
            doc: Lista com os dígitos base da Certidão.

        Returns:
            String com os dois dígitos verificadores.
        """
        first_digit = self._weighted_sum(doc) % 11
        if first_digit > 9:
            first_digit = 1

        second_digit = self._weighted_sum(doc + [first_digit]) % 11
        if second_digit > 9:
            second_digit = 1

        return str(first_digit) + str(second_digit)
