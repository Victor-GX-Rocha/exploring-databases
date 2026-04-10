""" Entities to safety converts diferents types of data and preservate DIP. """

from src.db.models.bases import ObjectConversor, OrmT, DtoT
from .rdsa_orm import RdsaHead, RdsaVisit
from .rdsa_dto import (
    HeadRecord, VisitRecord, 
    Treatment, Focal, Perifocal
)


class RdsaHeadConversor(ObjectConversor):
    def to_dto(self, orm: RdsaHead) -> HeadRecord:
        """ Converts the ORM information to a model. """
        return HeadRecord(head=orm.head)
    
    def to_orm(self, dto: HeadRecord) -> RdsaHead:
        """  """
        return RdsaHead(
            municipality=dto.municipality,
            locality_code=dto.locality_code,
            locality_name=dto.locality_name,
            locality_category=dto.locality_category,
            zone_number_and_name=dto.zone_number_and_name,
            zone_type=dto.zone_type,
            zone_concluded=dto.zone_concluded,
            activity_date=dto.activity_date,
            cicle_year=dto.cicle_year,
            activity_type=dto.activity_type
        )

class RdsaVisitConversor(ObjectConversor):
    def to_dto(self, orm: RdsaVisit) -> VisitRecord:
        """ Converts the ORM information toa a model. """
        
        return VisitRecord(
            visit=orm.visit,
            num_deposits=orm.num_deposits,
            sample_collection=orm.sample_collection,
            treatment=Treatment(
                eliminated_deposits=orm.eliminated_deposits,
                treated_property=orm.treated_property,
                focal=Focal(
                    type_l1=orm.focal_type_l1,
                    quantity_load=orm.focal_quantity_load,
                    treated_deposits_quantity=orm.focal_treated_deposits_quantity
                ),
                perifocal=Perifocal(
                    type_=orm.perifocal_type,
                    quantity_load=orm.perifocal_quantity_load
                ),
            )
        )
    
    def to_orm(self, dto: VisitRecord) -> RdsaVisit:
        """  """
        
        return RdsaVisit(
            # visit
            block_number=dto.visit.block_number,
            sequence=dto.visit.sequence,
            side=dto.visit.side,
            entrance_name=dto.visit.entrance_name,
            number=dto.visit.number,
            sequence_2=dto.visit.sequence_2,
            complement=dto.visit.complement,
            property_type=dto.visit.property_type,
            visite_time=dto.visit.visite_time,
            visite_type=dto.visit.visite_type,
            pendence=dto.visit.pendence,
            
            # num_deposits
            a1=dto.num_deposits.a1,
            a2=dto.num_deposits.a2,
            b=dto.num_deposits.b,
            c=dto.num_deposits.c,
            d1=dto.num_deposits.d1,
            d2=dto.num_deposits.d2,
            e=dto.num_deposits.e,
            inspecioned_property_quantity=dto.num_deposits.inspecioned_property_quantity,
            
            # sample_collection
            num_initial_sample=dto.sample_collection.num_initial_sample,
            num_final_sample=dto.sample_collection.num_final_sample,
            quantity_tubes=dto.sample_collection.quantity_tubes,
            
            # treatment
            eliminated_deposits=dto.eliminated_deposits,
            treated_property=dto.treated_property,
            focal_type_l1=dto.focal.focal_type_l1,
            focal_quantity_load=dto.focal.focal_quantity_load,
            focal_treated_deposits_quantity=dto.focal.focal_treated_deposits_quantity,
            perifocal_type=dto.perifocal.perifocal_type,
            perifocal_quantity_load=dto.perifocal.perifocal_quantity_load
        )


__all__ = [
    'RdsaHeadConversor',
    'RdsaVisitConversor'
]
