"""  """

from typing import TypeVar, Generic
from abc import ABC, abstractmethod


OrmT = TypeVar('OrmT')
DtoT = TypeVar('DtoT')


class ObjectConversor(ABC, Generic[OrmT, DtoT]):
    @abstractmethod
    def to_dto(self, orm: OrmT) -> DtoT:
        """ Converts a DTO to a ORM. """
        raise NotImplementedError
    
    @abstractmethod
    def to_orm(self, dto: DtoT) -> OrmT:
        """ Converts an ORM to a DTO. """
        raise NotImplementedError


__all__ = [
    'ObjectConversor'
]
