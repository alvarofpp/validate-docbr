import inspect

from validate_docbr.DocumentBase import DocumentBase


def validate_docs(documents: list[tuple[type[DocumentBase], str]] = list) -> list[bool]:
    """Recebe uma lista de tuplas (classe, valor) e valida cada documento.

    Args:
        documents: Lista de tuplas onde o primeiro elemento é a classe
            do documento (subclasse de ``DocumentBase``) e o segundo
            é o valor a ser validado.

    Returns:
        Lista de booleanos indicando a validade de cada documento.

    Raises:
        TypeError: Se o primeiro elemento da tupla não for uma
            subclasse de ``DocumentBase``.
    """
    validations = []

    for doc_class, doc_value in documents:
        if not inspect.isclass(doc_class) or not issubclass(doc_class, DocumentBase):
            raise TypeError(
                "O primeiro índice da tupla deve ser uma classe de documento!"
            )

        validations.append(doc_class().validate(doc_value))

    return validations
