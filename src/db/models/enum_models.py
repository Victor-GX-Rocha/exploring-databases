""" Enums and fixed data """

from enum import Enum

class ZoneType(Enum):
    """
    Args:
        SEDE (int): 
        OUTROS (int): 
    """
    SEDE: int = 1
    OUTROS: int = 2

class ZoneConcluded(Enum):
    """
    Args:
        SIM (str):
        NAO (str):
    """
    SIM: str = 'S'
    NAO: str = 'N'

class ActvityType(Enum):
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

class PropertyType(Enum):
    """  """

class VisiteType(Enum):
    """
    
    Args:
        NORMAL (str): 
        RECUP (str): 
    """
    NORMAL: str = 'N'
    RECUP: str = 'R'

class Pendence(Enum):
    """
    Reason why visit didn't happened.
    
    Args:
        FECHADO (str): The property was closed.
        RECUSA (str): The resident refuse the visit.
    """
    FECHADO: str = 'F'
    RECUSA: str = 'R'



class LocalityCategory(Enum):
    """  """


class FocalTypeL1(Enum):
    """  """

class PerifocalType(Enum):
    """  """


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
