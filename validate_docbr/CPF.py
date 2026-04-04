from random import sample

from validate_docbr.DocumentBase import DocumentBase


class CPF(DocumentBase):
    """Classe referente ao Cadastro de Pessoas Físicas (CPF)."""

    def __init__(self, repeated_digits: bool = False) -> None:
        self.digits = list(range(10))
        self.repeated_digits = repeated_digits

    def validate(self, doc: str = '') -> bool:
        """Valida o CPF.

        Args:
            doc: CPF a ser validado. Aceita com ou sem máscara.

        Returns:
            True se o CPF for válido, False caso contrário.
        """
        if not self._validate_input(doc, ['.', '-']):
            return False

        doc = list(self._only_digits(doc))

        if len(doc) > 11:
            return False

        if len(doc) < 11:
            doc = self._complete_with_zeros(doc)

        if not self.repeated_digits and self._check_repeated_digits(doc):
            return False

        return self._generate_first_digit(doc) == doc[9] \
            and self._generate_second_digit(doc) == doc[10]

    def generate(self, mask: bool = False) -> str:
        """Gera um CPF válido.

        Args:
            mask: Se True, retorna o CPF formatado (ex: ``012.345.678-90``).

        Returns:
            CPF gerado em formato string.
        """
        cpf = [str(sample(self.digits, 1)[0]) for _ in range(9)]

        cpf.append(self._generate_first_digit(cpf))
        cpf.append(self._generate_second_digit(cpf))

        cpf = "".join(cpf)

        return self.mask(cpf) if mask else cpf

    def mask(self, doc: str = '') -> str:
        """Coloca a máscara de CPF no documento.

        Args:
            doc: CPF sem máscara (11 dígitos).

        Returns:
            CPF formatado no padrão ``XXX.XXX.XXX-XX``.
        """
        return f"{doc[:3]}.{doc[3:6]}.{doc[6:9]}-{doc[-2:]}"

    def _generate_first_digit(self, doc: list) -> str:
        """Gera o primeiro dígito verificador do CPF.

        Args:
            doc: Lista com os dígitos do CPF.

        Returns:
            Primeiro dígito verificador.
        """
        total = 0

        for weight in range(10, 1, -1):
            total += int(doc[10 - weight]) * weight

        total = (total * 10) % 11

        if total == 10:
            total = 0

        return str(total)

    def _generate_second_digit(self, doc: list) -> str:
        """Gera o segundo dígito verificador do CPF.

        Args:
            doc: Lista com os dígitos do CPF.

        Returns:
            Segundo dígito verificador.
        """
        total = 0

        for weight in range(11, 1, -1):
            total += int(doc[11 - weight]) * weight

        total = (total * 10) % 11

        if total == 10:
            total = 0

        return str(total)

    def _check_repeated_digits(self, doc: list[str]) -> bool:
        """Verifica se é um CPF com números repetidos.

        Exemplo: ``111.111.111-11``.

        Args:
            doc: Lista com os dígitos do CPF.

        Returns:
            True se todos os dígitos forem iguais.
        """
        return len(set(doc)) == 1

    def _complete_with_zeros(self, doc: str) -> list[str]:
        """Adiciona zeros à esquerda para completar o CPF.

        Args:
            doc: Lista com os dígitos do CPF incompleto.

        Returns:
            Lista com 11 dígitos, preenchida com zeros à esquerda.
        """
        zeros_needed = 11 - len(doc)
        return ['0'] * zeros_needed + doc
