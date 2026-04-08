""" Dataclasses and data hierarchy estructures """

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from .enum_models import (
    ZoneType,
    ZoneConcluded,
    ActvityType,
    PropertyType,
    VisiteType,
    Pendence,
    LocalityCategory,
    FocalTypeL1,
    PerifocalType
)


@dataclass
class DTOHead:
    """
    Args:
        municipality (str):
        locality_code (int):
        locality_name (str):
        locality_category (LocalityCategory):
        zone_number_and_name (str):
        zone_type (ZoneType):
        zone_concluded (ZoneConcluded):
        activity_date (Date):
        cicle_year (str):
        activity (ActvityType):
    """
    municipality: str
    locality_code: int
    locality_name: str
    locality_category: LocalityCategory
    zone_number_and_name: str
    zone_type: ZoneType
    zone_concluded: ZoneConcluded
    activity_date: datetime
    cicle_year: str
    activity: ActvityType

@dataclass
class DTOVisit:
    """
    Informations about the locality and property during the visit.
    
    Args:
        block_number (int): 
        sequence (int): 
        side (int): 
        entrance_name (str): 
        number (int): 
        sequence_2 (int): 
        complement (int): 
        property_type (Enum): 
        visite_time (datetime): 
        visite_type (Enum): 
        pendence (Enum): 
    """
    block_number: int
    sequence: int
    side: int
    entrance_name: str
    number: int
    sequence_2: int
    complement: int
    property_type: PropertyType
    visite_time: datetime
    visite_type: VisiteType
    pendence: Pendence

@dataclass
class DTONumDeposits:
    """
    
    Args:
        a1 (int): 
        a2 (int): 
        b (int): 
        c (int): 
        d1 (int): 
        d2 (int): 
        e (int): 
        inspecioned_property_quantity (int): 
    """
    a1: int = 0
    a2: int = 0
    b: int = 0
    c: int = 0
    d1: int = 0
    d2: int = 0
    e: int = 0
    inspecioned_property_quantity: int = 0

@dataclass
class DTOSampleCollection:
    """
    
    Args:
        num_initial_sample (int):
        num_final_sample (int):
        quantity_tubes (int):
    """
    num_initial_sample: Optional[int] = None
    num_final_sample: Optional[int] = None
    quantity_tubes: Optional[int] = None

@dataclass
class DTOFocal:
    """  """
    type_l1: FocalTypeL1
    quantity_load: int
    treated_deposits_quantity: int

@dataclass
class DTOPerifocal:
    """  """
    type_: PerifocalType
    quantity_load: int

@dataclass
class DTOTreatment:
    eliminated_deposits: int
    treated_property: int
    focal: DTOFocal
    perifocal: DTOPerifocal
    

@dataclass
class DTORDSA:
    """
    Por enquanto vou criar isso aqui dentro mesmo.
    """
    head: DTOHead
    visit: DTOVisit
    num_deposits: DTONumDeposits
    sample_collection: DTOSampleCollection
    treatment: DTOTreatment


__all__ = [
    'DTOHead',
    'DTOVisit',
    'DTONumDeposits',
    'DTOSampleCollection',
    'DTOFocal',
    'DTOPerifocal',
    'DTOTreatment',
    'DTORDSA'
]
