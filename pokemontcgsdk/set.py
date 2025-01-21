from dataclasses import dataclass
from typing import Optional

from pokemontcgsdk.legality import Legality
from pokemontcgsdk.querybuilder import QueryBuilder
from pokemontcgsdk.setimage import SetImage

@dataclass
class Set():
    RESOURCE = 'sets'

    id: str
    images: Optional[SetImage]
    legalities: Optional[Legality]
    name: Optional[str]
    printedTotal: Optional[int]
    ptcgoCode: Optional[str]
    releaseDate: Optional[str]
    series: Optional[str]
    total: Optional[int]
    updatedAt: Optional[str]


    @staticmethod
    def find(id):
        return QueryBuilder(Set).find(id)

    @staticmethod
    def where(**kwargs):
        return QueryBuilder(Set).where(**kwargs)

    @staticmethod
    def all():
        return QueryBuilder(Set).all()
