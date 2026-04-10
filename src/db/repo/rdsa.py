""" A basic CRUD system for table RDSA. """

from typing import Optional

from src.db.connection import session_scope
from src.db.models.rdsa.rdsa_orm import RdsaHead, RdsaVisit
from src.db.models.rdsa.rdsa_dto import (
    Visit, NumDeposits,
    HeadRecord, VisitRecord
)
from src.db.models.rdsa.rdsa_conversor import RdsaHeadConversor, RdsaVisitConversor
from src.db.models.bases import ObjectConversor 


class RdsaHeadRepository:
    def __init__(self, conversor: Optional[ObjectConversor] = None):
        self.conversor = conversor or RdsaHeadConversor()
    
    def create(self, head: HeadRecord) -> None:
        """  """
        with session_scope() as session:
            session.add(self.conversor.to_orm(head))

class RdsaVistRepository:
    def __init__(self, conversor: Optional[ObjectConversor] = None):
        self.conversor = conversor or RdsaVisitConversor()
    
    def create(self, visit: VisitRecord) -> None:
        """  """
        with session_scope() as session:
            session.add(self.conversor.to_orm(visit))


__all__ = [
    'RdsaHeadRepository',
    'RdsaVistRepository'
]
