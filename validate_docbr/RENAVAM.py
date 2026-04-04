from random import sample

from validate_docbr.DocumentBase import DocumentBase


class RENAVAM(DocumentBase):
    """Classe referente ao Registro Nacional de Veículos Automotores (RENAVAM)."""

    WEIGHTS = [3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    def __init__(self) -> None:
        self.digits = list(range(10))

    def validate(self, doc: str = '') -> bool:
        """Valida o RENAVAM.

        Args:
            doc: RENAVAM a ser validado. Aceita com ou sem máscara.

        Returns:
            True se o RENAVAM for válido, False caso contrário.
        """
        if not self._validate_input(doc, [' ', '-']):
            return False

        doc = self._only_digits(doc)

        if len(doc) != 11:
            return False

        last_digit = self._generate_last_digit(doc)

        return last_digit == doc[10]

    def generate(self, mask: bool = False) -> str:
        """Gera um RENAVAM válido.

        Args:
            mask: Se True, retorna o RENAVAM formatado
                (ex: ``XXXXXXXXXX-X``).

        Returns:
            RENAVAM gerado em formato string.
        """
        renavam = [str(sample(self.digits, 1)[0]) for _ in range(10)]
        renavam.append(self._generate_last_digit(renavam))

        renavam = ''.join(renavam)
        return self.mask(renavam) if mask else renavam

    def mask(self, doc: str = '') -> str:
        """Coloca a máscara de RENAVAM no documento.

        Args:
            doc: RENAVAM sem máscara (11 dígitos).

        Returns:
            RENAVAM formatado no padrão ``XXXXXXXXXX-X``.
        """
        return f"{doc[:10]}-{doc[10]}"

    def _generate_last_digit(self, doc: str | list[str]) -> str:
        """Gera o dígito verificador do RENAVAM.

        Args:
            doc: String ou lista com os dígitos do RENAVAM.

        Returns:
            Dígito verificador.
        """
        total = sum(
            int(doc[position]) * self.WEIGHTS[position]
            for position in range(10)
        )

        remainder = (total * 10) % 11

        if remainder == 10:
            remainder = 0

        return str(remainder)
