from typing import Type

from address.dar_schemas.adresse import Adresse
from address.dar_schemas.adressepunkt import Adressepunkt
from address.dar_schemas.husnummer import Husnummer
from address.dar_schemas.navngiven_vej import NavngivenVej
from address.dar_schemas.navngiven_vej import NavngivenVejKommunedel
from address.dar_schemas.navngiven_vej import NavngivenVejPostnummer
from address.dar_schemas.navngiven_vej import NavngivenVejSupplerendeBynavn
from address.dar_schemas.navngiven_vej import Postnummer
from address.dar_schemas.supplerende_bynavn import SupplerendeBynavn
from pydantic import BaseModel

dar_root_objects: dict[str, Type[BaseModel]] = {
    "AdresseList": Adresse,
    "AdressepunktList": Adressepunkt,
    "HusnummerList": Husnummer,
    "NavngivenVejList": NavngivenVej,
    "NavngivenVejKommunedelList": NavngivenVejKommunedel,
    "NavngivenVejPostnummerList": NavngivenVejPostnummer,
    "NavngivenVejSupplerendeBynavnList": NavngivenVejSupplerendeBynavn,
    "PostnummerList": Postnummer,
    "SupplerendeBynavnList": SupplerendeBynavn,
}
