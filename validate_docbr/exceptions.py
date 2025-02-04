class FunctionNotImplementedError(NotImplementedError):
    def __init__(self, function_name):
        super().__init__(f"The `{function_name}` function must be implemented.")
