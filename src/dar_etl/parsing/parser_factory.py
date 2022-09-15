from enum import Enum
from typing import Type

from pydantic import BaseModel

from dar_etl.parsing.parser import DarParser
from dar_etl.schemas.adresse import Adresse
from dar_etl.schemas.adressepunkt import Adressepunkt
from dar_etl.schemas.husnummer import Husnummer
from dar_etl.schemas.navngiven_vej import NavngivenVej
from dar_etl.schemas.navngiven_vej import NavngivenVejKommunedel
from dar_etl.schemas.navngiven_vej import NavngivenVejPostnummer
from dar_etl.schemas.navngiven_vej import NavngivenVejSupplerendeBynavn
from dar_etl.schemas.navngiven_vej import Postnummer
from dar_etl.schemas.root_keys import Root
from dar_etl.schemas.supplerende_bynavn import SupplerendeBynavn


class ParserFactory:
    _registry: dict[Root, Type[BaseModel]] = {
        Root.addresses: Adresse,
        Root.address_points: Adressepunkt,
        Root.house_numbers: Husnummer,
        Root.named_roads: NavngivenVej,
        Root.q1: NavngivenVejKommunedel,
        Root.q2: NavngivenVejPostnummer,
        Root.q3: NavngivenVejSupplerendeBynavn,
        Root.postal_codes: Postnummer,
        Root.q4: SupplerendeBynavn,
    }

    @classmethod
    def create(cls, root_key: Root) -> DarParser:
        return DarParser(
            parsing_type=cls._registry[root_key],
            root_key=root_key,
        )
