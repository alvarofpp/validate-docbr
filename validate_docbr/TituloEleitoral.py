from random import sample

from validate_docbr.DocumentBase import DocumentBase


class TituloEleitoral(DocumentBase):
    """Classe referente ao Título Eleitoral."""

    def __init__(self) -> None:
        self.digits = list(range(10))
        self.first_check_digit_weights = list(range(2, 10))
        self.second_check_digit_weights = list(range(7, 10))
        self.first_check_digit_doc_slice = slice(0, 8)
        self.second_check_digit_doc_slice = slice(8, 10)

    def validate(self, doc: str = '') -> bool:
        """Valida o Título Eleitoral.

        Args:
            doc: Título Eleitoral a ser validado. Aceita com ou sem máscara.

        Returns:
            True se o Título Eleitoral for válido, False caso contrário.
        """
        if not self._validate_input(doc, [' ']):
            return False

        doc_digits = list(map(int, self._only_digits(doc=doc)))

        if len(doc_digits) != 12:
            return False

        first_check_digit = self._compute_first_check_digit(doc_digits=doc_digits)
        second_check_digit = self._compute_second_check_digit(
            doc_digits=doc_digits,
            first_check_digit=first_check_digit
        )

        return first_check_digit == doc_digits[-2] \
            and second_check_digit == doc_digits[-1]

    def generate(self, mask: bool = False) -> str:
        """Gera um Título Eleitoral válido.

        Args:
            mask: Se True, retorna o Título formatado
                (ex: ``XXXX XXXX XXXX``).

        Returns:
            Título Eleitoral gerado em formato string.
        """
        document_digits = [sample(self.digits, 1)[0] for _ in range(8)]

        state_identifier = self._generate_valid_state_identifier()
        document_digits.extend(map(int, state_identifier))

        first_check_digit = self._compute_first_check_digit(doc_digits=document_digits)
        second_check_digit = self._compute_second_check_digit(
            doc_digits=document_digits,
            first_check_digit=first_check_digit
        )
        document_digits.extend([first_check_digit, second_check_digit])

        document = ''.join(map(str, document_digits))

        if mask:
            return self.mask(doc=document)

        return document

    def mask(self, doc: str = '') -> str:
        """Coloca a máscara de Título Eleitoral no documento.

        Args:
            doc: Título Eleitoral sem máscara (12 dígitos).

        Returns:
            Título Eleitoral formatado no padrão ``XXXX XXXX XXXX``.
        """
        return f'{doc[0:4]} {doc[4:8]} {doc[8:]}'

    def _compute_first_check_digit(self, doc_digits: list[int]) -> int:
        """Calcula o primeiro dígito verificador.

        Args:
            doc_digits: Lista com os dígitos do Título Eleitoral.

        Returns:
            Primeiro dígito verificador.
        """
        digits_to_consider = doc_digits[self.first_check_digit_doc_slice]
        total = sum(
            digit * weight
            for digit, weight in zip(digits_to_consider, self.first_check_digit_weights)
        )

        if total % 11 == 10:
            return 0

        return total % 11

    def _compute_second_check_digit(
            self,
            doc_digits: list[int],
            first_check_digit: int
    ) -> int:
        """Calcula o segundo dígito verificador.

        Args:
            doc_digits: Lista com os dígitos do Título Eleitoral.
            first_check_digit: Valor do primeiro dígito verificador.

        Returns:
            Segundo dígito verificador.
        """
        digits_to_consider = doc_digits[self.second_check_digit_doc_slice] \
                                + [first_check_digit]
        total = sum(
            digit * weight
            for digit, weight in zip(
                digits_to_consider,
                self.second_check_digit_weights,
            )
        )

        if total % 11 == 10:
            return 0

        return total % 11

    def _generate_valid_state_identifier(self) -> str:
        """Gera um identificador de estado válido.

        Returns:
            Identificador de estado com 2 dígitos (``01`` a ``18``).
        """
        state_identifier = str(sample(range(1, 19), 1)[0])
        return state_identifier.zfill(2)
