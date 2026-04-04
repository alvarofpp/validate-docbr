import string
from random import sample

from validate_docbr.DocumentBase import DocumentBase


class CNPJ(DocumentBase):
    """Classe referente ao Cadastro Nacional da Pessoa Jurídica (CNPJ).

    Aceita tanto o formato numérico tradicional quanto o novo formato
    alfanumérico. A validação reconhece ambos os formatos automaticamente.
    """

    def __init__(self) -> None:
        self.digits = list(range(10))
        self.digits_and_letters = list(string.ascii_uppercase) + list(string.digits)
        self.weights_first = list(range(5, 1, -1)) + list(range(9, 1, -1))
        self.weights_second = list(range(6, 1, -1)) + list(range(9, 1, -1))

    def validate(self, doc: str = '') -> bool:
        """Valida o CNPJ.

        Aceita tanto o formato numérico (``XX.XXX.XXX/XXXX-XX``) quanto o
        formato alfanumérico (``XX.XXX.XXX/XXXX-XX`` com letras).

        Args:
            doc: CNPJ a ser validado. Aceita com ou sem máscara.

        Returns:
            True se o CNPJ for válido, False caso contrário.
        """
        if not self._validate_input(doc, ['.', '/', '-'], allow_letters=True):
            return False

        doc = doc.strip().upper()
        doc = self._only_digits_and_letters(doc)

        if len(doc) != 14:
            return False

        return self._generate_first_digit(doc) == doc[12] \
               and self._generate_second_digit(doc) == doc[13]

    def generate(self, mask: bool = False, digits_only: bool = True) -> str:
        """Gera um CNPJ válido.

        Args:
            mask: Se True, retorna o CNPJ formatado
                (ex: ``12.345.678/0001-00``).
            digits_only: Se True, gera apenas com dígitos numéricos.
                Se False, gera no formato alfanumérico.

        Returns:
            CNPJ gerado em formato string.
        """
        if digits_only:
            cnpj = [str(sample(self.digits, 1)[0]) for _ in range(12)]
        else:
            cnpj = [sample(self.digits_and_letters, 1)[0] for _ in range(12)]

        cnpj.append(self._generate_first_digit(cnpj))
        cnpj.append(self._generate_second_digit(cnpj))

        cnpj = "".join(cnpj)

        return self.mask(cnpj) if mask else cnpj

    def mask(self, doc: str = '') -> str:
        """Coloca a máscara de CNPJ no documento.

        Args:
            doc: CNPJ sem máscara (14 caracteres).

        Returns:
            CNPJ formatado no padrão ``XX.XXX.XXX/XXXX-XX``.
        """
        return f"{doc[:2]}.{doc[2:5]}.{doc[5:8]}/{doc[8:12]}-{doc[-2:]}"

    def _generate_first_digit(self, doc: str | list[str]) -> str:
        """Gera o primeiro dígito verificador do CNPJ.

        Utiliza aritmética baseada em valores ASCII para suportar
        caracteres alfanuméricos.

        Args:
            doc: String ou lista com os caracteres do CNPJ.

        Returns:
            Primeiro dígito verificador.
        """
        total = sum(
            (ord(str(doc[position])) - 48) * self.weights_first[position]
            for position in range(12)
        )

        remainder = total % 11
        return str(0 if remainder < 2 else 11 - remainder)

    def _generate_second_digit(self, doc: str | list[str]) -> str:
        """Gera o segundo dígito verificador do CNPJ.

        Utiliza aritmética baseada em valores ASCII para suportar
        caracteres alfanuméricos.

        Args:
            doc: String ou lista com os caracteres do CNPJ.

        Returns:
            Segundo dígito verificador.
        """
        total = sum(
            (ord(str(doc[position])) - 48) * self.weights_second[position]
            for position in range(13)
        )

        remainder = total % 11
        return str(0 if remainder < 2 else 11 - remainder)
