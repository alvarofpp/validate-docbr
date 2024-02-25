from .BaseDoc import BaseDoc
from .Certidao import Certidao
from .CNH import CNH
from .CNPJ import CNPJ
from .CNS import CNS
from .CPF import CPF
from .generic import validate_docs
from .PIS import PIS
from .RENAVAM import RENAVAM
from .TituloEleitoral import TituloEleitoral

__all__ = [
    'BaseDoc',
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
