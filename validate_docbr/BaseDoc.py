from abc import ABC


class BaseDoc(ABC):
    """Classe base para todas as classes referentes a documentos."""

    def validate(self, doc):
        """Método para validar o documento desejado."""
        return

    def generate(self):
        """Método para gerar um documento válido."""
        return
