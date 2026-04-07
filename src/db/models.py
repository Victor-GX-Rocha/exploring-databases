""" ORM table models. """

from sqlalchemy import Integer, String, Text, Date
from sqlalchemy.orm import Mapped, mapped_column
from enum import Enum
from datetime import datetime

from src.db.connection import Base

class ZoneType(Enum):
    SEDE: int = 1
    OUTROS: int = 2

class ZoneConcluded(Enum):
    SIM: str = 'S'
    NAO: str = 'N'

class ActvityType(Enum):
    """ Essa atividade é um Enum gigantão, gosto de fazer as coisas bem auto documentadas, então deixa pra depois, vou fazer isso agora não porque vai dar trabalho e já é tarde kkkk """

class RDSA(Base):
    """
    ORM table to represents the sheet  "Resumo Diário de Serviço Antivetorial".
    """
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    
    """
    Blz, bora organizar e agrupar as coisas.
    Rever aquele meu código do mercado livre seria bem útil agora.
    Usar enums para trabalhar com dados fixos também pode ser bem vindo, tendo em vista que algumas coisas são padronizadas.
    
    A ideia é pegar e divdir esses quadros menores em sessões mais organizadas.
    
    1. Sobre a ficha/trabalho do dia.
    2. Pesquisa entomológica tratamento
        1. Localidade da residência.
        2. Número de depositos inspecionados.
        3. Coleta amostra.
        4. Tratamento.
    
    Por enquanto, só vai criando as colunas, depois tu pega e organiza direitinho.
    
    Vish, vendo agora, vou ter que por as coisas em português né? Fica mais intuitivo...
    Ou não também, mas de preferência não, vou ter que manter um padrão ao longo do código e o padrão que costuma mandar é o inglês.
    """
    
    # 1. Sobre a ficha/trabalho do dia.
    municipality: Mapped[str] = mapped_column(String(64), nullable=False)
    locality_code: Mapped[int] = mapped_column(Integer, nullable=False)
    locality_name: Mapped[str] = mapped_column(String(128))
    locality_category: Mapped[Enum] = mapped_column() # Essa parte aqui me pega, porque eu não sei o que vai aqui dentro, tenho que conversar com o Jhonata para entender que dados ele insere aqui, porque provavelmente é algo padronizado dentro de uma lista de categorias. De antemão vou deixar um Enum aqui.
    zone_number_and_name: Mapped[str] = mapped_column(String(128))
    zone_type: Mapped[Enum] = mapped_column(ZoneType)
    zone_concluded: Mapped[Enum] = mapped_column(ZoneConcluded)
    activity_date: Mapped[Date] = mapped_column(datetime)
    cicle_year: Mapped[str] = mapped_column(String(8)) # Vou deixar str por enquanto, pelo visto não parece ser uma data exatamente. mas tipo, ser o cliclo de inspeção (1, 2, 3, 4...) e o ano que ele ocorre (2025, 2026...), então tipo, não é uma data estilo mês e ano, mas sim duas informações separadas e distintas, cabe mais uma str aqui. Mas é bom tirar a dúvida com o ele para saber como é essa anotação.
    activity: Mapped[Enum] = mapped_column(ActvityType) 
    
    # 2.1. Localidade da residência.
    