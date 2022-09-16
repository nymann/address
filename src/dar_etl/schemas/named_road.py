from datetime import datetime
from typing import Optional

from pydantic import Field

from dar_etl.schemas.base_model import DarBaseModel


class NamedRoad(DarBaseModel):
    """
    EAID_0CB629B5_8D1F_486c_A319_717EDF879B82
    """

    administreres_af_kommune: Optional[str] = Field(
        None,
        alias="administreresAfKommune",
        description="EAID_31D3BE04_2F70_4092_8381_5517A5543634",
    )
    beskrivelse: Optional[str] = Field(None, description="EAID_C132D872_7F07_4ebf_BC6B_37049F2E5EB8")
    udtalt_vejnavn: Optional[str] = Field(
        None,
        alias="udtaltVejnavn",
        description="EAID_788F8478_A747_412d_9DE6_FEE0DB4C1BFA",
    )
    vejadresseringsnavn: Optional[str] = Field(None, description="EAID_9621DD9D_50E3_4426_AB5A_A5E43DED4B05")
    vejnavn: Optional[str] = Field(None, description="EAID_CA00150C_5B5C_4c32_AE72_A7EE5AEDE015")
    vejnavnebeliggenhed_oprindelse_kilde: Optional[str] = Field(
        None,
        description="EAID_4C594A8E_797B_40bb_B60D_0E5C9159DCD3.EAID_7F8EB510_AD02_4fd5_844B_C9AB17FB1798.EAID_FD77FC95_714B_4779_B7FA_F9BBAB41758D",
    )
    vejnavnebeliggenhed_oprindelse_nøjagtighedsklasse: Optional[str] = Field(
        None,
        description="EAID_4C594A8E_797B_40bb_B60D_0E5C9159DCD3.EAID_7F8EB510_AD02_4fd5_844B_C9AB17FB1798.EAID_B8A27494_DF27_4aa9_B1F4_EBD68D2479A5",
    )
    vejnavnebeliggenhed_oprindelse_registrering: Optional[datetime] = Field(
        None,
        description="EAID_4C594A8E_797B_40bb_B60D_0E5C9159DCD3.EAID_7F8EB510_AD02_4fd5_844B_C9AB17FB1798.EAID_10DCC555_0BE9_4991_AD8C_DEA595CB08A0",
    )
    vejnavnebeliggenhed_oprindelse_teknisk_standard: Optional[str] = Field(
        None,
        alias="vejnavnebeliggenhed_oprindelse_tekniskStandard",
        description="EAID_4C594A8E_797B_40bb_B60D_0E5C9159DCD3.EAID_7F8EB510_AD02_4fd5_844B_C9AB17FB1798.EAID_181528AD_2DA3_4e9d_BF38_81916A924D2A",
    )
    vejnavnebeliggenhed_vejnavnelinje: Optional[str] = Field(
        None,
        description="EAID_4C594A8E_797B_40bb_B60D_0E5C9159DCD3.EAID_93C24B4D_0641_4073_B260_1EC7F2024CF4",
    )
    vejnavnebeliggenhed_vejnavneområde: Optional[str] = Field(
        None,
        description="EAID_4C594A8E_797B_40bb_B60D_0E5C9159DCD3.EAID_1C496CD9_4541_4574_974D_B641F186077F",
    )
    vejnavnebeliggenhed_vejtilslutningspunkter: Optional[str] = Field(
        None,
        description="EAID_4C594A8E_797B_40bb_B60D_0E5C9159DCD3.EAID_C3E042F2_A66E_40f4_92A1_7C7024A30D16",
    )


class NavngivenVejKommunedel(DarBaseModel):
    """
    EAID_34D070E5_DD89_4984_8054_16BA70936EA0
    """

    kommune: Optional[str] = Field(None, description="EAID_0A04B5E9_9F12_49cb_B2AF_AFEE0315AE2B")
    vejkode: Optional[str] = Field(None, description="EAID_852A683F_3E30_4009_A003_B3C8F6F76930")
    navngiven_vej: Optional[str] = Field(
        None,
        alias="navngivenVej",
        description="EAID_dstE87A3E_ECA3_4f38_A586_117287E4754A",
    )


class NavngivenVejPostnummer(DarBaseModel):
    """
    EAID_EA75B9ED_59CD_4d67_A340_A1CB578CC1B7
    """

    navngiven_vej: Optional[str] = Field(
        None,
        alias="navngivenVej",
        description="EAID_1B3CAEB0_80FA_486f_ABD1_818B332C905C",
    )
    postnummer: Optional[str] = Field(None, description="EAID_AD2844E3_7F05_4d8d_967E_44BA3D12C4B4")


class NavngivenVejSupplerendeBynavn(DarBaseModel):
    """
    EAID_5F14BDC8_7D97_433b_B28D_F8A56A1B9F13
    """

    navngiven_vej: Optional[str] = Field(
        None,
        alias="navngivenVej",
        description="EAID_7CF789EC_31C0_4af3_B75B_77674A26DECD",
    )
    supplerende_bynavn: Optional[str] = Field(
        None,
        alias="supplerendeBynavn",
        description="EAID_21C0B8C7_8B67_406c_BDC1_21ADBA284867",
    )


class Postnummer(DarBaseModel):
    """
    EAID_449B3570_F0F7_494e_9756_D49E60644CD0
    """

    navn: Optional[str] = Field(None, description="EAID_9E7FA46D_52D9_4615_B24C_599BB28D1923")
    postnr: Optional[str] = Field(None, description="EAID_8F8BACBF_E985_4dc1_BCF4_27F5C3FD0BB1")
    postnummerinddeling: Optional[str] = Field(None, description="EAID_E5F5DDF9_3CF4_4304_B02D_E67AB0CDD619")
