""" enum.Enums and fixed data """

import enum


class ZoneType(enum.Enum):
    """
    Args:
        SEDE (int): 
        OUTROS (int): 
    """
    SEDE: int = 1
    OUTROS: int = 2

class ZoneConcluded(enum.Enum):
    """
    Args:
        SIM (str):
        NAO (str):
    """
    SIM: str = 'S'
    NAO: str = 'N'

class ActvityType(enum.Enum):
    """
    LI (int): Levantamento Indice.
    LI_T (int): Levantamento Indice e Tratamento.
    PE (int): Tratamento.
    T (int): Tratamento.
    DF (int): Delimitação de Foco.
    PVE (int): Pesquisa Vetorial Especial.
    """
    LI: int = 1
    LI_T: int = 2
    PE: int = 3
    T: int = 4
    DF: int = 5
    PVE: int = 6

class PropertyType(enum.Enum):
    """ Não sei o que por aqui no momento """
    dado_provisorio = None
    dado_provisorio_2 = None

class VisiteType(enum.Enum):
    """
    
    Args:
        NORMAL (str): 
        RECUP (str): 
    """
    NORMAL: str = 'N'
    RECUP: str = 'R'

class Pendence(enum.Enum):
    """
    Reason why visit didn't happened.
    
    Args:
        FECHADO (str): The property was closed.
        RECUSA (str): The resident refuse the visit.
    """
    FECHADO: str = 'F'
    RECUSA: str = 'R'



class LocalityCategory(enum.Enum):
    """ Não sei o que por aqui no momento """
    dado_provisorio = None
    dado_provisorio_2 = None

class FocalTypeL1(enum.Enum):
    """ Não sei o que por aqui no momento """
    dado_provisorio = None
    dado_provisorio_2 = None

class PerifocalType(enum.Enum):
    """ Não sei o que por aqui no momento """
    dado_provisorio = None
    dado_provisorio_2 = None


__all__ = [
    'ZoneType',
    'ZoneConcluded',
    'ActvityType',
    'PropertyType',
    'VisiteType',
    'Pendence',
    'LocalityCategory',
    'FocalTypeL1',
    'PerifocalType'
]
