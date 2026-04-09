""" ORM model for table "Resumo Diário do Serviço Antivetorial (RDSA)" """

from sqlalchemy import Integer, String, Date, Enum
from sqlalchemy.orm import Mapped, mapped_column, composite
from datetime import datetime
import enum

from src.db.connection import Base
from .rdsa_enum import (
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
from .rdsa_dto import (
    DTOHead,
    DTOVisit,
    DTONumDeposits,
    DTOSampleCollection,
    DTOFocal,
    DTOPerifocal,
    DTOTreatment,
    DTORDSA
)

class RDSA(Base):
    """
    An ORM class to represents the "Resumo Diário do Serviço Antivetorial (RDSA)" as a table.
    
    Keeps all the informations during a ACE visit.
    """
    
    __tablename__ = 'RDSA'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    municipality: Mapped[str] = mapped_column(String(64), nullable=False)
    locality_code: Mapped[int] = mapped_column(Integer, nullable=False)
    locality_name: Mapped[str] = mapped_column(String(128), nullable=False)
    locality_category: Mapped[enum.Enum] = mapped_column(Enum(LocalityCategory))
    zone_number_and_name: Mapped[str] = mapped_column(String(128))
    zone_type: Mapped[enum.Enum] = mapped_column(Enum(ZoneType))
    zone_concluded: Mapped[enum.Enum] = mapped_column(Enum(ZoneConcluded))
    activity_date: Mapped[datetime] = mapped_column(Date)
    cicle_year: Mapped[str] = mapped_column(String(8))
    activity_type: Mapped[enum.Enum] = mapped_column(Enum(ActvityType))
    
    head = composite(
        DTOHead,
        'municipality',
        'locality_code',
        'locality_name',
        'locality_category',
        'zone_number_and_name',
        'zone_type',
        'zone_concluded',
        'activity_date',
        'cicle_year',
        'activity_type'
    )
    
    # 2.1. Localidade da residência.
    block_number: Mapped[int] = mapped_column(Integer)
    sequence: Mapped[int] = mapped_column(Integer)
    side: Mapped[int] = mapped_column(Integer)
    entrance_name: Mapped[str] = mapped_column(String(128))
    number: Mapped[int] = mapped_column(Integer)
    sequence_2: Mapped[int] = mapped_column(Integer)
    complement: Mapped[int] = mapped_column(Integer)
    property_type: Mapped[enum.Enum] = mapped_column(Enum(PropertyType))
    visite_time: Mapped[datetime] = mapped_column(Date)
    visite_type: Mapped[enum.Enum] = mapped_column(Enum(VisiteType))
    pendence: Mapped[enum.Enum] = mapped_column(Enum(Pendence))
    
    visit = composite(
        DTOVisit,
        'block_number',
        'sequence',
        'side',
        'entrance_name',
        'number',
        'sequence_2',
        'complement',
        'property_type',
        'visite_time',
        'visite_type',
        'pendence',
    )
    
    # 2.2. Número de depositos inspecionados.
    a1: Mapped[int] = mapped_column(Integer)
    a2: Mapped[int] = mapped_column(Integer)
    b: Mapped[int] = mapped_column(Integer)
    c: Mapped[int] = mapped_column(Integer)
    d1: Mapped[int] = mapped_column(Integer)
    d2: Mapped[int] = mapped_column(Integer)
    e: Mapped[int] = mapped_column(Integer)
    inspecioned_property_quantity: Mapped[int] = mapped_column(Integer)
    
    num_deposits = composite(
        DTONumDeposits,
        'a1',
        'a2',
        'b',
        'c',
        'd1',
        'd2',
        'e',
        'inspecioned_property_quantity'
    )
    
    # 2.3.1 Coleta amostra.
    num_initial_sample: Mapped[int] = mapped_column(Integer)
    num_final_sample: Mapped[int] = mapped_column(Integer)
    quantity_tubes: Mapped[int] = mapped_column(Integer)
    
    sample_collection = composite(
        DTOSampleCollection,
        'num_initial_sample',
        'num_final_sample',
        'quantity_tubes'
    )
    
    
    # 2.3.2 Tratamento.
    eliminated_deposits: Mapped[int] = mapped_column(Integer)
    treated_property: Mapped[int] = mapped_column(Integer)
    # 2.4.1 Focal larvicida
    focal_type_l1: Mapped[enum.Enum] = mapped_column(Enum(FocalTypeL1))
    focal_quantity_load: Mapped[int] = mapped_column(Integer)
    focal_treated_deposits_quantity: Mapped[int] = mapped_column(Integer)
    # 2.4.2 Perifocal adulticida
    perifocal_type: Mapped[enum.Enum] = mapped_column(Enum(PerifocalType))
    perifocal_quantity_load: Mapped[int] = mapped_column(Integer)
    
    # treatment = composite(
    #     DTOTreatment,
    #     'eliminated_deposits',
    #     'treated_property',
    #     'focal_type_l1',
    #     'focal_quantity_load',
    #     'focal_treated_deposits_quantity',
    #     'perifocal_type',
    #     'perifocal_quantity_load'
    # )
    
    def to_dto(self) -> DTORDSA:
        """ Converts the ORM information toa a model. """
        
        return DTORDSA(
            head=DTOHead(self.head),
            visit=DTOVisit(self.visit),
            num_deposits=DTONumDeposits(self.num_deposits),
            sample_collection=DTOSampleCollection(self.sample_collection),
            treatment=DTOTreatment(
                eliminated_deposits=self.eliminated_deposits,
                treated_property=self.treated_property,
                focal=DTOFocal(
                    type_l1=self.focal_type_l1,
                    quantity_load=self.focal_quantity_load,
                    treated_deposits_quantity=self.focal_treated_deposits_quantity
                ),
                perifocal=DTOPerifocal(
                    type_=self.perifocal_type,
                    quantity_load=self.perifocal_quantity_load
                ),
            )
        )


__all__ = [
    'RDSA'
]
