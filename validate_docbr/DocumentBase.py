import re
from abc import ABC, abstractmethod

from validate_docbr.exceptions import FunctionNotImplementedError


class DocumentBase(ABC):
    """Classe base para todas as classes referentes a documentos."""

    @abstractmethod
    def validate(self, doc: str = "") -> bool:
        """Método para validar o documento desejado.

        Args:
            doc: Documento a ser validado.

        Returns:
            True se o documento for válido, False caso contrário.
        """
        raise FunctionNotImplementedError("validate")

    @abstractmethod
    def generate(self, mask: bool = False) -> str:
        """Método para gerar um documento válido.

        Args:
            mask: Se True, retorna o documento formatado com máscara.

        Returns:
            Documento gerado em formato string.
        """
        raise FunctionNotImplementedError("generate")

    @abstractmethod
    def mask(self, doc: str = '') -> str:
        """Mascara o documento enviado.

        Args:
            doc: Documento a ser mascarado.

        Returns:
            Documento formatado com a máscara.
        """
        raise FunctionNotImplementedError("mask")

    def validate_list(self, docs: list[str]) -> list[bool]:
        """Método para validar uma lista de documentos.

        Args:
            docs: Lista de documentos a serem validados.

        Returns:
            Lista de booleanos indicando a validade de cada documento.
        """
        return [self.validate(doc) for doc in docs]

    def generate_list(
        self,
        number_of_documents: int = 1,
        mask: bool = False,
        repeat: bool = False
    ) -> list:
        """Gerar uma lista do mesmo tipo de documento.

        Args:
            number_of_documents: Quantidade de documentos a serem gerados.
            mask: Se True, os documentos gerados terão máscara.
            repeat: Se True, permite documentos repetidos.

        Returns:
            Lista de documentos gerados.
        """
        if number_of_documents <= 0:
            return []

        doc_list = [self.generate(mask) for _ in range(number_of_documents)]

        while not repeat:
            doc_set = set(doc_list)
            unique_count = len(doc_set)

            if unique_count < number_of_documents:
                doc_list = list(doc_set) + self.generate_list(
                    (number_of_documents - unique_count), mask, repeat
                )
            else:
                repeat = True

        return doc_list

    def _only_digits(self, doc: str = "") -> str:
        """Remove os outros caracteres que não sejam dígitos.

        Args:
            doc: String de entrada.

        Returns:
            String contendo apenas os dígitos.
        """
        return "".join(char for char in doc if char.isdigit())

    def _only_digits_and_letters(self, doc: str = "") -> str:
        """Remove os outros caracteres que não sejam dígitos ou letras.

        Args:
            doc: String de entrada.

        Returns:
            String contendo apenas dígitos e letras.
        """
        return "".join(char for char in doc if char.isdigit() or char.isalpha())

    def _validate_input(
        self,
        doc: str,
        valid_characters: list[str] | None = None,
        allow_letters: bool = False,
    ) -> bool:
        """Valida se o input contém apenas caracteres permitidos usando RegEx.

        Verifica se o documento contém apenas dígitos (e, opcionalmente,
        letras) e caracteres especiais válidos.

        Args:
            doc: Documento a ser validado.
            valid_characters: Lista de caracteres especiais permitidos.
                Padrão: ``[".", "-", "/", " "]``.
            allow_letters: Se True, permite letras além de dígitos.

        Returns:
            True se o input contém apenas caracteres permitidos,
            False caso contrário.
        """
        if valid_characters is None:
            valid_characters = [".", "-", "/", " "]

        escaped_chars = ''.join(re.escape(char) for char in valid_characters)

        if allow_letters:
            pattern = rf'^[\da-zA-Z{escaped_chars}]*$'
        else:
            pattern = rf'^[\d{escaped_chars}]*$'

        return bool(re.match(pattern, doc))
