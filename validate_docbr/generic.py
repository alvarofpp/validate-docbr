import inspect

from .DocumentBase import DocumentBase


def validate_docs(documents: list[tuple[type[DocumentBase], str]] = list()):
    """Recebe uma lista de tuplas (classe, valor) e a valida"""
    validations = []

    for doc in documents:
        if not inspect.isclass(doc[0]) or not issubclass(doc[0], DocumentBase):
            raise TypeError(
                "O primeiro índice da tupla deve ser uma classe de documento!"
            )

        validations.append(doc[0]().validate(doc[1]))

    return validations
