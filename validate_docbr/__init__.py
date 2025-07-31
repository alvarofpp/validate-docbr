from .Certidao import Certidao
from .CNH import CNH
from .CNPJ import CNPJ
from .CNS import CNS
from .CPF import CPF
from .DocumentBase import DocumentBase
from .generic import validate_docs
from .PIS import PIS
from .RENAVAM import RENAVAM
from .TituloEleitoral import TituloEleitoral

__all__ = [
    'DocumentBase',
    'CPF',
    'CNPJ',
    'CNH',
    'CNS',
    'PIS',
    'TituloEleitoral',
    'Certidao',
    'RENAVAM',
    'validate_docs',
]
