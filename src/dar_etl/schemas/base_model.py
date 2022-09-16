from datetime import datetime
from enum import Enum
from typing import Any, Optional

from devtools import debug
from pydantic import BaseModel
from pydantic import Field


class Status(Enum):
    """https://danmarksadresser.dk/adressedata/kodelister/livscyklus/"""

    INTERNAL_PREPERATION = "1"
    PRELIMINARY = "2"
    APPLICABLE = "3"
    DISCONTINUED = "4"
    ARCHIVED = "5"
    DELETED = "6"
    NOT_IN_USE = "7"
    IN_USE = "8"
    OBSOLETE = "9"
    EXPIRED = "10"
    TERMINATED = "11"


class BusinessProcess(Enum):
    """https://danmarksadresser.dk/adressedata/kodelister/forretningsproces"""

    MASTER_DATA = "0"  # Stamdata
    ADDRESS_ASSIGNMENT = "1"  # Adresseopgave
    DIALOG_CLIENT = "2"  # Dialogklient
    STREET_POSTCODE = "3"  # Gadepostnummer
    SUPPLEMENTARY_CITY_NAME = "4"  # Supplerendebynavn
    ERROR_REPORTING_CLIENT = "5"  # Fejlmeldeklient
    UNDONE_FORWARD_DATING = "6"  # Fortrudt fremdatering


class BusinessArea(Enum):
    DAR = "54.15.10.25"  # Danmarks Adresse Register, DAR
    POSTAL_CODES = "54.15.10.15"  # Postnumre
    ROAD_NAMES_AND_ROAD_CODES = "54.15.10.06"  # Vejnavne og vejkoder
    HOUSE_NUMBER = "54.15.10.07"  # Husnummer
    ADDRESSES = "54.15.10.08"  # Adresser
    UNKNOWN1 = "10.00.00.00"
    UNKNOWN = "UNKNOWN"

    @classmethod
    def _missing_(cls, business_area: str) -> Any:
        return cls(cls.UNKNOWN)


class BusinessEvent(Enum):
    NAMED_ROAD = "0"  # Navngivenvej
    NAMED_ROAD_MUNICIPAL_DISTRICT = "1"  # NavngivenvejKommunedel
    ADDRESS = "2"  # Adresse
    HOUSE_NUMBER = "3"  # Husnummer
    POSTAL_CODE = "4"  # Postnummer
    SUPPLEMENTARY_CITY_NAME = "5"  # Supplerendebynavn
    HOUSE_NUMBER_RESERVATION = "6"  # Husnummerreservation
    ROAD_NAME_RESERVATION = "7"  # VejnavnReservation
    ADDRESS_ASSIGNMENT = "8"  # Adresseopgave
    ADDRESS_ASSIGNMENT_ITEM = "9"  # Adresseopgavegenstand
    DAGI_MUNICIPALITY = "10"  # DAGIKommune
    DAGI_PARISH_DIVISION = "11"  # DAGISogneinddeling
    DAGI_POSTAL_CODE = "12"  # DAGIPostnummer
    DAGI_VOTING_AREA = "13"  # DAGIAfstemningsområde
    DAGI_PARISH_COUNCIL_VOTING_AREA = "14"  # DAGIMeninghedsrådsafstemningsområde
    DAGI_SUPPLEMENTARY_CITY_NAME = "15"  # DAGISupplerendeBynavn
    BBR_BUILDING = "16"  # BBRBygning
    BBR_TECHNICAL_PLANT = "17"  # BBRTekniskanlæg
    MU_PIECE_OF_LAND = "18"  # MUJordstykke (matriklens udvidelse)
    GEO_DANMARK_BUILDING = "19"  # GeoDanmarkBygning
    GEO_DANMARK_WAYPOINT = "20"  # GeoDanmarkVejmidte


class DarBaseModel(BaseModel):
    business_event: Optional[BusinessEvent] = Field(
        None,
        alias="forretningshændelse",
        description="Den forretningshændelse, som afstedkom opdateringen af adresseelementet til den pågældende version",
    )
    business_area: Optional[BusinessArea] = Field(
        None,
        alias="forretningsområde",
        description="Det forretningsområde som har opdateret adresseelementet til den pågældende version",
    )
    business_process: Optional[BusinessProcess] = Field(
        None,
        alias="forretningsproces",
        description="Den forretningsproces, som afstedkom opdateringen af adresseelementet til den pågældende version",
    )
    id_namespace: Optional[str] = Field(
        None,
        alias="id_namespace",
        description="EAID_D273E3D8_A3F4_41bc_AF9C_E67B4A29C008.EAID_6CEB0356_5CBF_4159_B96B_A2489DD2DAC8",
    )
    id_local: Optional[str] = Field(
        None,
        alias="id_lokalId",
        description="Identifikation af adresseelementet igennem hele dets livscyklus.",
    )
    registration_from: Optional[datetime] = Field(
        None,
        alias="registreringFra",
        description="Tidspunktet hvor registreringen af den pågældende version af adresseelementet er foretaget",
    )
    registration_operator: Optional[str] = Field(
        None,
        description="Den aktør der har foretaget registreringen af den pågældende version af adresseelementet",
        alias="registreringsaktør",
    )
    registration_to: Optional[datetime] = Field(
        None,
        alias="registreringTil",
        description="Tidspunktet hvor en ny registrering på adresseelementet er foretaget, og hvor denne version således ikke længere er den seneste.",
    )
    status: Optional[Status] = Field(
        None,
        alias="status",
        description="Adresseelementets status i den pågældende version, dvs. elementets tilstand i den samlede livscyklus",
    )
    effect_from: Optional[datetime] = Field(
        None,
        alias="virkningFra",
        description="Tidspunktet hvorfra den pågældende version af adresseelementet har virkning",
    )
    effect_to: Optional[datetime] = Field(
        None,
        alias="virkningTil",
        description="Tidspunktet hvor virkningen af den pågældende version af adresseelementet ophører",
    )
    effector: Optional[str] = Field(
        None,
        alias="virkningsaktør",
        description="Den aktør der har afstedkommet virkningsegenskaberne for den pågældende version af adresseelementet",
    )
