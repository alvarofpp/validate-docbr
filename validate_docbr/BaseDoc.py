from abc import ABC


class BaseDoc(ABC):
    """Classe base para todas as classes referentes a documentos."""

    def validate(self, doc: str) -> bool:
        """Método para validar o documento desejado."""
        pass

    def generate(self, mask: bool = False) -> str:
        """Método para gerar um documento válido."""
        pass

    def mask(self, doc: str) -> str:
        """Mascara o documento enviado"""
        pass

    def _only_digits(self, doc: str) -> str:
        """Remove os outros caracteres que não sejam dígitos."""
        return "".join([x for x in doc if x.isdigit()])
