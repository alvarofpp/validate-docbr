import abc


class BaseDoc:
    """Classe base para todas as classes referentes a documentos."""

    @staticmethod
    @abc.abstractmethod
    def validate(self, doc):
        """Método para validar o documento desejado."""
        return

    @staticmethod
    @abc.abstractmethod
    def generate(self):
        """Método para gerar um documento válido."""
        return
