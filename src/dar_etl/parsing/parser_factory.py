from collections.abc import Iterable
from typing import Type

from pydantic import BaseModel

from dar_etl.parsing.parser import DarParser
from dar_etl.schemas.address import Adresse
from dar_etl.schemas.address_point import AddressPoint
from dar_etl.schemas.house_number import HouseNumber
from dar_etl.schemas.named_road import NamedRoad
from dar_etl.schemas.named_road import NavngivenVejKommunedel
from dar_etl.schemas.named_road import NavngivenVejPostnummer
from dar_etl.schemas.named_road import NavngivenVejSupplerendeBynavn
from dar_etl.schemas.named_road import Postnummer
from dar_etl.schemas.root_keys import Root
from dar_etl.schemas.supplerende_bynavn import SupplerendeBynavn


class ParserFactory:
    _registry: dict[Root, Type[BaseModel]] = {
        # Root.addresses: Adresse,
        # Root.address_points: AddressPoint,
        Root.house_numbers: HouseNumber,
        Root.named_roads: NamedRoad,
        Root.q1: NavngivenVejKommunedel,
        Root.q2: NavngivenVejPostnummer,
        Root.q3: NavngivenVejSupplerendeBynavn,
        Root.postal_codes: Postnummer,
        Root.q4: SupplerendeBynavn,
    }

    @classmethod
    def create(cls, root: Root) -> DarParser:
        return DarParser(
            parsing_type=cls._registry[root],
            root=root,
        )

    @classmethod
    def create_all(cls) -> Iterable[DarParser]:
        for root, parsing_type in cls._registry.items():
            yield DarParser(parsing_type=parsing_type, root=root)
