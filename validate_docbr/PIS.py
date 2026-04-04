from random import sample

from validate_docbr.DocumentBase import DocumentBase


class PIS(DocumentBase):
    """Classe referente ao PIS/NIS/PASEP/NIT."""

    MULTIPLIERS = [3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    def __init__(self) -> None:
        self.digits = list(range(10))

    def validate(self, doc: str = '') -> bool:
        """Valida o PIS/NIS/PASEP/NIT.

        Args:
            doc: PIS a ser validado. Aceita com ou sem máscara.

        Returns:
            True se o PIS for válido, False caso contrário.
        """
        if not self._validate_input(doc, ['.', '-']):
            return False

        doc = self._only_digits(doc)

        if len(doc) != 11 or self._is_repeated_digits(doc):
            return False

        digit = self._generate_digit(doc)

        return digit == doc[10]

    def generate(self, mask: bool = False) -> str:
        """Gera um PIS/NIS/PASEP/NIT válido.

        Args:
            mask: Se True, retorna o PIS formatado
                (ex: ``XXX.XXXXX.XX-X``).

        Returns:
            PIS gerado em formato string.
        """
        pis = [str(sample(self.digits, 1)[0]) for _ in range(10)]
        pis.append(self._generate_digit(pis))

        pis = ''.join(pis)
        return self.mask(pis) if mask else pis

    def mask(self, doc: str = '') -> str:
        """Coloca a máscara de PIS/NIS/PASEP/NIT no documento.

        Args:
            doc: PIS sem máscara (11 dígitos).

        Returns:
            PIS formatado no padrão ``XXX.XXXXX.XX-X``.
        """
        return f"{doc[:3]}.{doc[3:8]}.{doc[8:10]}-{doc[10:]}"

    def _generate_digit(self, doc: str | list[str]) -> str:
        """Gera o dígito verificador do PIS/NIS/PASEP/NIT.

        Args:
            doc: String ou lista com os dígitos do PIS.

        Returns:
            Dígito verificador.
        """
        total = sum(
            int(doc[position]) * self.MULTIPLIERS[position]
            for position in range(10)
        )

        remainder = total % 11
        digit = 0 if remainder < 2 else 11 - remainder

        return str(digit)

    def _is_repeated_digits(self, doc: str) -> bool:
        """Verifica se o PIS/NIS/PASEP/NIT contém apenas números repetidos.

        Exemplo: ``11111111111``.

        Args:
            doc: String com os dígitos do PIS.

        Returns:
            True se todos os dígitos forem iguais.
        """
        return len(set(doc)) == 1
