from random import sample

from validate_docbr.DocumentBase import DocumentBase


class CNS(DocumentBase):
    """Classe referente ao Cartão Nacional de Saúde (CNS)."""

    def __init__(self) -> None:
        self.digits = list(range(10))
        self.first_digit = [1, 2, 7, 8, 9]

    def validate(self, doc: str = '') -> bool:
        """Valida o CNS.

        Args:
            doc: CNS a ser validado. Aceita com ou sem máscara.

        Returns:
            True se o CNS for válido, False caso contrário.
        """
        if not self._validate_input(doc, [' ']):
            return False

        doc = list(self._only_digits(doc))

        if len(doc) != 15 or int(doc[0]) not in self.first_digit:
            return False

        return self._check_cns_valid(doc)

    def _validate_first_case(self, doc: list) -> bool:
        """Valida CNSs que comecem com 1 ou 2.

        Args:
            doc: Lista com os dígitos do CNS.

        Returns:
            True se o CNS for válido.
        """
        cns = self._generate_first_case(doc)
        return cns == doc

    def _validate_second_case(self, doc: list) -> bool:
        """Valida CNSs que comecem com 7, 8 ou 9.

        Args:
            doc: Lista com os dígitos do CNS.

        Returns:
            True se o CNS for válido.
        """
        total = self._weighted_sum(doc)
        return total % 11 == 0

    def generate(self, mask: bool = False) -> str:
        """Gera um CNS válido.

        Args:
            mask: Se True, retorna o CNS formatado
                (ex: ``XXX XXXX XXXX XXXX``).

        Returns:
            CNS gerado em formato string.
        """
        cns = [str(sample(self.first_digit, 1)[0])]

        if cns[0] in ['1', '2']:
            cns = self._generate_first_case(cns, random_digits=True)
        else:
            cns = self._generate_second_case(cns)

        cns = ''.join(cns)

        return self.mask(cns) if mask else cns

    def mask(self, doc: str = '') -> str:
        """Coloca a máscara de CNS no documento.

        Args:
            doc: CNS sem máscara (15 dígitos).

        Returns:
            CNS formatado no padrão ``XXX XXXX XXXX XXXX``.
        """
        return f"{doc[:3]} {doc[3:7]} {doc[7:11]} {doc[-4:]}"

    def _generate_first_case(self, cns: list, random_digits: bool = False) -> list:
        """Gera um CNS válido para os casos que se iniciam com 1 ou 2.

        Args:
            cns: Lista com os dígitos iniciais do CNS.
            random_digits: Se True, gera dígitos aleatórios para completar.

        Returns:
            Lista com os 15 dígitos do CNS gerado.
        """
        if random_digits:
            cns = cns + [str(sample(self.digits, 1)[0]) for _ in range(10)]
        else:
            cns = cns[:11]

        total = self._weighted_sum(cns, 11)
        check_digit = 11 - (total % 11)

        if check_digit == 11:
            check_digit = 0

        if check_digit == 10:
            total += 2
            check_digit = 11 - (total % 11)
            cns = cns + ['0', '0', '1', str(check_digit)]
        else:
            cns = cns + ['0', '0', '0', str(check_digit)]

        return cns

    def _generate_second_case(self, cns: list) -> list:
        """Gera um CNS válido para os casos que se iniciam com 7, 8 ou 9.

        Args:
            cns: Lista com o primeiro dígito do CNS.

        Returns:
            Lista com os 15 dígitos do CNS gerado.
        """
        cns = cns + [str(sample(list(range(10)), 1)[0]) for _ in range(14)]
        total = self._weighted_sum(cns)
        remainder = total % 11

        if remainder == 0:
            return cns

        diff = 11 - remainder
        return self._adjust_cns(cns, 15 - diff, diff)

    def _adjust_cns(self, cns: list, position: int, remainder: int) -> list:
        """Ajusta o CNS recursivamente para que atenda as regras de validade.

        Args:
            cns: Lista com os dígitos do CNS.
            position: Posição atual sendo ajustada.
            remainder: Valor restante para ajuste.

        Returns:
            Lista com os dígitos do CNS válido.
        """
        if remainder == 0:
            if self._check_cns_valid(cns):
                return cns
            total = self._weighted_sum(cns)
            diff = 15 - (total % 11)
            return self._adjust_cns(cns, 15 - diff, diff)

        if 15 - position > remainder:
            return self._adjust_cns(cns, position + 1, remainder)

        if cns[position] != '9':
            cns[position] = str(int(cns[position]) + 1)
            remainder -= (15 - position)
        else:
            remainder += (15 - position)
            cns[position] = str(int(cns[position]) - 1)
            position -= 1

        return self._adjust_cns(cns, position, remainder)

    def _weighted_sum(self, cns: list, length: int = 15) -> int:
        """Realiza o processo de soma ponderada necessária para o CNS.

        Args:
            cns: Lista com os dígitos do CNS.
            length: Quantidade de dígitos a considerar na soma.

        Returns:
            Resultado da soma ponderada.
        """
        return sum(int(cns[position]) * (15 - position) for position in range(length))

    def _check_cns_valid(self, cns: list) -> bool:
        """Verifica se o CNS é válido de acordo com o primeiro dígito.

        Args:
            cns: Lista com os dígitos do CNS.

        Returns:
            True se o CNS for válido.
        """
        if cns[0] in ['1', '2']:
            return self._validate_first_case(cns)
        return self._validate_second_case(cns)
