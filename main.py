""" Execution file """

from src.db.connection import create_tables
from src.db.repo.rdsa import RdsaHeadRepository
from src.db.models.rdsa.rdsa_dto import HeadRecord
from src.db.models.rdsa.rdsa_enum import (
    LocalityCategory,
    ZoneType,
    ZoneConcluded,
    ActvityType
)
from datetime import datetime

def main() -> None:
    """ Execution function """
    create_tables()
    repo_head = RdsaHeadRepository()
    
    head = HeadRecord(
        municipality='Croatá',
        locality_code=1,
        locality_name='Betânia',
        locality_category=LocalityCategory.dado_provisorio,
        zone_number_and_name='Nome e número da zona',
        zone_type=ZoneType.SEDE,
        zone_concluded=ZoneConcluded.NAO,
        activity_date=datetime.now(),
        cicle_year='Cilco / ano',
        activity_type=ActvityType.LI
    )
    
    repo_head.create(head)
    # repo_head.delete(2)

if __name__ == '__main__':
    main()
