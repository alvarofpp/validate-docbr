from .BaseDoc import BaseDoc
from random import sample


class CNS(BaseDoc):
    """Classe referente ao Cartão Nacional de Saúde (CNS)."""

    def __init__(self):
        self.digits = list(range(10))
        self.first_digit = [1, 2, 7, 8, 9]

    def validate(self, doc: str = '') -> bool:
        """Validar CNS."""
        doc = list(self._only_digits(doc))

        if len(doc) != 15 or int(doc[0]) not in self.first_digit:
            return False

        return self._check_cns_valid(doc)

    def _validate_first_case(self, doc: list) -> bool:
        """Validar CNSs que comecem com 1 ou 2."""
        cns = self._generate_first_case(doc)

        return cns == doc

    def _validate_second_case(self, doc: list) -> bool:
        """Validar CNSs que comecem com 7, 8 ou 9."""
        sum = self._sum_algorithm(doc)

        return sum % 11 == 0

    def generate(self, mask: bool = False) -> str:
        """Gerar CNS."""
        # Primeiro dígito válido
        cns = [str(sample(self.first_digit, 1)[0])]

        # Geração irá depender do resultado do primeiro dígito
        if cns[0] in ['1', '2']:
            cns = self._generate_first_case(cns, True)
        else:
            cns = self._generate_second_case(cns)

        cns = "".join(cns)

        return self.mask(cns) if mask else cns

    def mask(self, doc: str = '') -> str:
        """Coloca a máscara de CPF na variável doc."""
        return "{} {} {} {}".format(doc[:3], doc[3:7], doc[7:11], doc[-4:])

    def _generate_first_case(self, cns: list, generate_random=False) -> list:
        """Gera um CNS válido para os casos que se inicia com 1 ou 2."""
        if generate_random:
            # Adiciona os próximos 10 dígitos
            cns = cns + [str(sample(self.digits, 1)[0]) for i in range(10)]
        else:
            # Pega apenas a parte que precisamos do CNS
            cns = cns[:11]

        # Processo de soma
        sum = self._sum_algorithm(cns, 11)

        dv = 11 - (sum % 11)

        if dv == 11:
            dv = 0

        if dv == 10:
            sum += 2
            dv = 11 - (sum % 11)
            cns = cns + ['0', '0', '1', str(dv)]
        else:
            cns = cns + ['0', '0', '0', str(dv)]

        return cns

    def _generate_second_case(self, cns: list) -> list:
        """Gera um CNS válido para os casos que se inicia com 7, 8 ou 9."""
        # Gerar os próximos 14 dígitos
        cns = cns + [str(sample(list(range(10)), 1)[0]) for i in range(14)]
        sum = self._sum_algorithm(cns)
        rest = sum % 11

        if rest == 0:
            return cns

        # Resto para o próximo múltiplo de 11
        diff = 11 - rest

        # Verificar qual é o mais próximo
        return self._change_cns(cns, 15 - diff, diff)

    def _change_cns(self, cns: list, i: int, val: int) -> list:
        """Altera o CNS recursivamente para que atenda as especificações de validade dele."""
        if val == 0:
            if self._check_cns_valid(cns):
                return cns
            else:
                sum = self._sum_algorithm(cns)
                diff = 15 - (sum % 11)
                return self._change_cns(cns, 15 - diff, diff)

        if 15 - i > val:
            i += 1
            return self._change_cns(cns, i, val)

        if not cns[i] == '9':
            cns[i] = str(int(cns[i]) + 1)
            val -= (15 - i)
        else:
            val += (15 - i)
            cns[i] = str(int(cns[i]) - 1)
            i -= 1

        return self._change_cns(cns, i, val)

    def _sum_algorithm(self, cns: list, n: int = 15) -> int:
        """Realiza o processo de soma necessária para o CNS."""
        sum = 0
        for i in range(n):
            sum += int(cns[i]) * (15 - i)

        return sum

    def _check_cns_valid(self, cns: list) -> bool:
        """Checa se o CNS é válido."""
        if cns[0] in ['1', '2']:
            return self._validate_first_case(cns)
        else:
            return self._validate_second_case(cns)
