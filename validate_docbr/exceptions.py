class FunctionNotImplementedError(NotImplementedError):
    """Exceção para métodos abstratos não implementados.

    Args:
        function_name: Nome da função que não foi implementada.
    """

    def __init__(self, function_name: str) -> None:
        super().__init__(f"The `{function_name}` function must be implemented.")
