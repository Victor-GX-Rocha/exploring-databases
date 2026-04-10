""" ORM model for table "Resumo Diário do Serviço Antivetorial (RDSA)" """

from sqlalchemy import Integer, String, Date, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, composite, relationship
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
    HeadRecord,
    VisitRecord,
    NumDeposits,
    SampleCollection,
    Focal,
    Perifocal,
    Treatment,
    Visit
)

class RdsaHead(Base):
    """
    An ORM class to represents the "Resumo Diário do Serviço Antivetorial (RDSA)" heading as a table.
    
    Pretends to Keep all the informations about a work day.
    """
    
    __tablename__ = 'rdsa_head'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    
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
        HeadRecord,
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
    
    rdsa_visit = relationship('RdsaVisit', back_populates='rdsa_head', lazy='selectin')


class RdsaVisit(Base):
    """
    An ORM class to represents the "Resumo Diário do Serviço Antivetorial (RDSA)" heading as a table.
    
    Pretends to Keep all the informations during a ACE each visit.
    """
    
    __tablename__ = 'rdsa_visit'
    
    rdsa_head = relationship('RdsaHead', back_populates='rdsa_visit')
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    
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
        Visit,
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
        'pendence'
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
        NumDeposits,
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
        SampleCollection,
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
    
    head_id: Mapped[int] = mapped_column(ForeignKey('rdsa_head.id'))



__all__ = [
    'RdsaHead',
    'RdsaVisit'
]
