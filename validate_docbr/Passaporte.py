import re
from random import choices

from validate_docbr.DocumentBase import DocumentBase


class Passaporte(DocumentBase):
    """Classe para validar e gerar números de Passaporte Brasileiro."""

    def __init__(self) -> None:
        self.regex = re.compile(r"^[A-Z]{2}\d{7}$", re.IGNORECASE)

    def validate(self, doc: str = '') -> bool:
        """Valida o Passaporte.

        Args:
            doc: Passaporte a ser validado. Aceita com ou sem máscara.

        Returns:
            True se o Passaporte for válido, False caso contrário.
        """
        if not self._validate_input(doc, [' ', '-'], allow_letters=True):
            return False

        clean_doc = self._only_digits_and_letters(doc)

        return bool(self.regex.fullmatch(clean_doc))

    def generate(self, mask: bool = False) -> str:
        """Gera um Passaporte válido.

        Args:
            mask: Se True, retorna o Passaporte formatado.

        Returns:
            Passaporte gerado em formato string.
        """
        letters = "".join(choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=2))
        numbers = "".join(choices("0123456789", k=7))

        passport = f"{letters}{numbers}"
        return self.mask(passport) if mask else passport

    def mask(self, doc: str = '') -> str:
        """Coloca a máscara de Passaporte no documento.

        Args:
            doc: Passaporte com ou sem máscara.

        Returns:
            Passaporte formatado no padrão ``XX-XXXXXXX``.
        """
        doc = self._only_digits_and_letters(doc)
        return f"{doc[:2]}-{doc[2:]}"
