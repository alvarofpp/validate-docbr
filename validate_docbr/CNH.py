from random import sample

from validate_docbr.DocumentBase import DocumentBase


class CNH(DocumentBase):
    """Classe referente à Carteira Nacional de Habilitação (CNH)."""

    def __init__(self) -> None:
        self.digits = list(range(10))

    def validate(self, doc: str = '') -> bool:
        """Valida a CNH.

        Args:
            doc: CNH a ser validada. Aceita com ou sem máscara.

        Returns:
            True se a CNH for válida, False caso contrário.
        """
        if not self._validate_input(doc, [' ']):
            return False

        doc = self._only_digits(doc)

        if len(doc) != 11 or self._is_repeated_digits(doc):
            return False

        first_digit = self._generate_first_digit(doc)
        second_digit = self._generate_second_digit(doc)

        return first_digit == doc[9] and second_digit == doc[10]

    def generate(self, mask: bool = False) -> str:
        """Gera uma CNH válida.

        Args:
            mask: Se True, retorna a CNH formatada (ex: ``XXX XXX XXX XX``).

        Returns:
            CNH gerada em formato string.
        """
        cnh = [str(sample(self.digits, 1)[0]) for _ in range(9)]
        cnh.append(self._generate_first_digit(cnh))
        cnh.append(self._generate_second_digit(cnh))

        cnh = ''.join(cnh)
        return self.mask(cnh) if mask else cnh

    def mask(self, doc: str = '') -> str:
        """Coloca a máscara de CNH no documento.

        Args:
            doc: CNH sem máscara (11 dígitos).

        Returns:
            CNH formatada no padrão ``XXX XXX XXX XX``.
        """
        return f"{doc[:3]} {doc[3:6]} {doc[6:9]} {doc[9:]}"

    def _generate_first_digit(self, doc: str | list[str]) -> str:
        """Gera o primeiro dígito verificador da CNH.

        Também define o valor de desconto (``_dsc``) utilizado no cálculo
        do segundo dígito verificador.

        Args:
            doc: String ou lista com os dígitos da CNH.

        Returns:
            Primeiro dígito verificador.
        """
        self._dsc = 0
        total = 0

        for weight in range(9, 0, -1):
            total += int(doc[9 - weight]) * weight

        first_value = total % 11
        if first_value >= 10:
            first_value, self._dsc = 0, 2

        return str(first_value)

    def _generate_second_digit(self, doc: str | list[str]) -> str:
        """Gera o segundo dígito verificador da CNH.

        Utiliza o valor de desconto (``_dsc``) calculado pelo primeiro
        dígito verificador.

        Args:
            doc: String ou lista com os dígitos da CNH.

        Returns:
            Segundo dígito verificador.
        """
        total = 0

        for weight in range(1, 10):
            total += int(doc[weight - 1]) * weight

        remainder = total % 11

        second_value = remainder - self._dsc
        if second_value < 0:
            second_value += 11
        if second_value >= 10:
            second_value = 0

        return str(second_value)

    def _is_repeated_digits(self, doc: str) -> bool:
        """Verifica se a CNH contém apenas números repetidos.

        Exemplo: ``11111111111``.

        Args:
            doc: String com os dígitos da CNH.

        Returns:
            True se todos os dígitos forem iguais.
        """
        return len(set(doc)) == 1
