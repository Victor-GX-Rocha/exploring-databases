""" Execution file """

from src.db.connection import create_tables
from src.db.models.rdsa_orm import RDSA 

def main() -> None:
    """ Execution function """
    create_tables()

if __name__ == '__main__':
    main()
