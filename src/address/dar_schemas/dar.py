from pydantic import BaseModel
from pydantic import Field

from address.dar_schemas.addresse import Adresse
from address.dar_schemas.addressepunkt import Adressepunkt
from address.dar_schemas.husnummer import Husnummer
from address.dar_schemas.navngiven_vej import NavngivenVej
from address.dar_schemas.navngiven_vej import NavngivenVejKommunedel
from address.dar_schemas.navngiven_vej import NavngivenVejPostnummer
from address.dar_schemas.navngiven_vej import NavngivenVejSupplerendeBynavn
from address.dar_schemas.navngiven_vej import Postnummer
from address.dar_schemas.supplerende_bynavn import SupplerendeBynavn


class DAR(BaseModel):
    adresse_list: list[Adresse] = Field(list, alias="AdresseList")
    adressepunkt_list: list[Adressepunkt] = Field(list, alias="AdressepunktList")
    husnummer_list: list[Husnummer] = Field(list, alias="HusnummerList")
    navngiven_vej_list: list[NavngivenVej] = Field(list, alias="NavngivenVejList")
    navngiven_vej_kommunedel_list: list[NavngivenVejKommunedel] = Field(list, alias="NavngivenVejKommunedelList")
    navngiven_vej_postnummer_list: list[NavngivenVejPostnummer] = Field(list, alias="NavngivenVejPostnummerList")
    navngiven_vej_supplerende_bynavn_list: list[NavngivenVejSupplerendeBynavn] = Field(
        list,
        alias="NavngivenVejSupplerendeBynavnList",
    )
    postnummer_list: list[Postnummer] = Field(list, alias="PostnummerList")
    supplerende_bynavn_list: list[SupplerendeBynavn] = Field(list, alias="SupplerendeBynavnList")
