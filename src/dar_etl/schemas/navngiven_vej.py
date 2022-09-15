from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class NavngivenVej(BaseModel):
    """
    EAID_0CB629B5_8D1F_486c_A319_717EDF879B82
    """

    forretningshændelse: Optional[str] = Field(None, description="EAID_1CE948DD_FC3D_4638_8913_A2D35A00F64D")
    forretningsområde: Optional[str] = Field(None, description="EAID_C955CFEC_E2A0_47da_9F76_6452FCC9E4E2")
    forretningsproces: Optional[str] = Field(None, description="EAID_A9A40479_E58D_4c7a_A0EA_F8EC4829ECAC")
    id_namespace: Optional[str] = Field(
        None,
        description="EAID_D273E3D8_A3F4_41bc_AF9C_E67B4A29C008.EAID_6CEB0356_5CBF_4159_B96B_A2489DD2DAC8",
    )
    id_lokal_id: Optional[str] = Field(
        None,
        alias="id_lokalId",
        description="EAID_D273E3D8_A3F4_41bc_AF9C_E67B4A29C008.EAID_9AB90AE0_9F85_4164_9B25_8EB2139D65A5",
    )
    registrering_fra: Optional[datetime] = Field(
        None,
        alias="registreringFra",
        description="EAID_96862BAA_95CA_46aa_A6A0_757327A10BF7",
    )
    registreringsaktør: Optional[str] = Field(None, description="EAID_9F724D2B_7763_4997_8C85_580610BABC1F")
    registrering_til: Optional[datetime] = Field(
        None,
        alias="registreringTil",
        description="EAID_301BF58F_26E7_4d1f_B7B6_3881F8C1B0A5",
    )
    status: Optional[str] = Field(None, description="EAID_22AF1E6A_73A8_4c89_96EB_C307235DFD19")
    virkning_fra: Optional[datetime] = Field(
        None,
        alias="virkningFra",
        description="EAID_AB768062_FD24_4960_8AA1_C6BFF90C00C5",
    )
    virkningsaktør: Optional[str] = Field(None, description="EAID_8E60197F_D857_47c6_8611_75B63D0940FD")
    virkning_til: Optional[datetime] = Field(
        None,
        alias="virkningTil",
        description="EAID_3058C5FD_9824_48ba_B62C_C24587BF6537",
    )
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


class NavngivenVejKommunedel(BaseModel):
    """
    EAID_34D070E5_DD89_4984_8054_16BA70936EA0
    """

    forretningshændelse: Optional[str] = Field(None, description="EAID_1CE948DD_FC3D_4638_8913_A2D35A00F64D")
    forretningsområde: Optional[str] = Field(None, description="EAID_C955CFEC_E2A0_47da_9F76_6452FCC9E4E2")
    forretningsproces: Optional[str] = Field(None, description="EAID_A9A40479_E58D_4c7a_A0EA_F8EC4829ECAC")
    id_namespace: Optional[str] = Field(
        None,
        description="EAID_D273E3D8_A3F4_41bc_AF9C_E67B4A29C008.EAID_6CEB0356_5CBF_4159_B96B_A2489DD2DAC8",
    )
    id_lokal_id: Optional[str] = Field(
        None,
        alias="id_lokalId",
        description="EAID_D273E3D8_A3F4_41bc_AF9C_E67B4A29C008.EAID_9AB90AE0_9F85_4164_9B25_8EB2139D65A5",
    )
    registrering_fra: Optional[datetime] = Field(
        None,
        alias="registreringFra",
        description="EAID_96862BAA_95CA_46aa_A6A0_757327A10BF7",
    )
    registreringsaktør: Optional[str] = Field(None, description="EAID_9F724D2B_7763_4997_8C85_580610BABC1F")
    registrering_til: Optional[datetime] = Field(
        None,
        alias="registreringTil",
        description="EAID_301BF58F_26E7_4d1f_B7B6_3881F8C1B0A5",
    )
    status: Optional[str] = Field(None, description="EAID_22AF1E6A_73A8_4c89_96EB_C307235DFD19")
    virkning_fra: Optional[datetime] = Field(
        None,
        alias="virkningFra",
        description="EAID_AB768062_FD24_4960_8AA1_C6BFF90C00C5",
    )
    virkningsaktør: Optional[str] = Field(None, description="EAID_8E60197F_D857_47c6_8611_75B63D0940FD")
    virkning_til: Optional[datetime] = Field(
        None,
        alias="virkningTil",
        description="EAID_3058C5FD_9824_48ba_B62C_C24587BF6537",
    )
    kommune: Optional[str] = Field(None, description="EAID_0A04B5E9_9F12_49cb_B2AF_AFEE0315AE2B")
    vejkode: Optional[str] = Field(None, description="EAID_852A683F_3E30_4009_A003_B3C8F6F76930")
    navngiven_vej: Optional[str] = Field(
        None,
        alias="navngivenVej",
        description="EAID_dstE87A3E_ECA3_4f38_A586_117287E4754A",
    )


class NavngivenVejPostnummer(BaseModel):
    """
    EAID_EA75B9ED_59CD_4d67_A340_A1CB578CC1B7
    """

    forretningshændelse: Optional[str] = Field(None, description="EAID_1CE948DD_FC3D_4638_8913_A2D35A00F64D")
    forretningsområde: Optional[str] = Field(None, description="EAID_C955CFEC_E2A0_47da_9F76_6452FCC9E4E2")
    forretningsproces: Optional[str] = Field(None, description="EAID_A9A40479_E58D_4c7a_A0EA_F8EC4829ECAC")
    id_namespace: Optional[str] = Field(
        None,
        description="EAID_D273E3D8_A3F4_41bc_AF9C_E67B4A29C008.EAID_6CEB0356_5CBF_4159_B96B_A2489DD2DAC8",
    )
    id_lokal_id: Optional[str] = Field(
        None,
        alias="id_lokalId",
        description="EAID_D273E3D8_A3F4_41bc_AF9C_E67B4A29C008.EAID_9AB90AE0_9F85_4164_9B25_8EB2139D65A5",
    )
    registrering_fra: Optional[datetime] = Field(
        None,
        alias="registreringFra",
        description="EAID_96862BAA_95CA_46aa_A6A0_757327A10BF7",
    )
    registreringsaktør: Optional[str] = Field(None, description="EAID_9F724D2B_7763_4997_8C85_580610BABC1F")
    registrering_til: Optional[datetime] = Field(
        None,
        alias="registreringTil",
        description="EAID_301BF58F_26E7_4d1f_B7B6_3881F8C1B0A5",
    )
    status: Optional[str] = Field(None, description="EAID_22AF1E6A_73A8_4c89_96EB_C307235DFD19")
    virkning_fra: Optional[datetime] = Field(
        None,
        alias="virkningFra",
        description="EAID_AB768062_FD24_4960_8AA1_C6BFF90C00C5",
    )
    virkningsaktør: Optional[str] = Field(None, description="EAID_8E60197F_D857_47c6_8611_75B63D0940FD")
    virkning_til: Optional[datetime] = Field(
        None,
        alias="virkningTil",
        description="EAID_3058C5FD_9824_48ba_B62C_C24587BF6537",
    )
    navngiven_vej: Optional[str] = Field(
        None,
        alias="navngivenVej",
        description="EAID_1B3CAEB0_80FA_486f_ABD1_818B332C905C",
    )
    postnummer: Optional[str] = Field(None, description="EAID_AD2844E3_7F05_4d8d_967E_44BA3D12C4B4")


class NavngivenVejSupplerendeBynavn(BaseModel):
    """
    EAID_5F14BDC8_7D97_433b_B28D_F8A56A1B9F13
    """

    forretningshændelse: Optional[str] = Field(None, description="EAID_1CE948DD_FC3D_4638_8913_A2D35A00F64D")
    forretningsområde: Optional[str] = Field(None, description="EAID_C955CFEC_E2A0_47da_9F76_6452FCC9E4E2")
    forretningsproces: Optional[str] = Field(None, description="EAID_A9A40479_E58D_4c7a_A0EA_F8EC4829ECAC")
    id_namespace: Optional[str] = Field(
        None,
        description="EAID_D273E3D8_A3F4_41bc_AF9C_E67B4A29C008.EAID_6CEB0356_5CBF_4159_B96B_A2489DD2DAC8",
    )
    id_lokal_id: Optional[str] = Field(
        None,
        alias="id_lokalId",
        description="EAID_D273E3D8_A3F4_41bc_AF9C_E67B4A29C008.EAID_9AB90AE0_9F85_4164_9B25_8EB2139D65A5",
    )
    registrering_fra: Optional[datetime] = Field(
        None,
        alias="registreringFra",
        description="EAID_96862BAA_95CA_46aa_A6A0_757327A10BF7",
    )
    registreringsaktør: Optional[str] = Field(None, description="EAID_9F724D2B_7763_4997_8C85_580610BABC1F")
    registrering_til: Optional[datetime] = Field(
        None,
        alias="registreringTil",
        description="EAID_301BF58F_26E7_4d1f_B7B6_3881F8C1B0A5",
    )
    status: Optional[str] = Field(None, description="EAID_22AF1E6A_73A8_4c89_96EB_C307235DFD19")
    virkning_fra: Optional[datetime] = Field(
        None,
        alias="virkningFra",
        description="EAID_AB768062_FD24_4960_8AA1_C6BFF90C00C5",
    )
    virkningsaktør: Optional[str] = Field(None, description="EAID_8E60197F_D857_47c6_8611_75B63D0940FD")
    virkning_til: Optional[datetime] = Field(
        None,
        alias="virkningTil",
        description="EAID_3058C5FD_9824_48ba_B62C_C24587BF6537",
    )
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


class Postnummer(BaseModel):
    """
    EAID_449B3570_F0F7_494e_9756_D49E60644CD0
    """

    forretningshændelse: Optional[str] = Field(None, description="EAID_1CE948DD_FC3D_4638_8913_A2D35A00F64D")
    forretningsområde: Optional[str] = Field(None, description="EAID_C955CFEC_E2A0_47da_9F76_6452FCC9E4E2")
    forretningsproces: Optional[str] = Field(None, description="EAID_A9A40479_E58D_4c7a_A0EA_F8EC4829ECAC")
    id_namespace: Optional[str] = Field(
        None,
        description="EAID_D273E3D8_A3F4_41bc_AF9C_E67B4A29C008.EAID_6CEB0356_5CBF_4159_B96B_A2489DD2DAC8",
    )
    id_lokal_id: Optional[str] = Field(
        None,
        alias="id_lokalId",
        description="EAID_D273E3D8_A3F4_41bc_AF9C_E67B4A29C008.EAID_9AB90AE0_9F85_4164_9B25_8EB2139D65A5",
    )
    registrering_fra: Optional[datetime] = Field(
        None,
        alias="registreringFra",
        description="EAID_96862BAA_95CA_46aa_A6A0_757327A10BF7",
    )
    registreringsaktør: Optional[str] = Field(None, description="EAID_9F724D2B_7763_4997_8C85_580610BABC1F")
    registrering_til: Optional[datetime] = Field(
        None,
        alias="registreringTil",
        description="EAID_301BF58F_26E7_4d1f_B7B6_3881F8C1B0A5",
    )
    status: Optional[str] = Field(None, description="EAID_22AF1E6A_73A8_4c89_96EB_C307235DFD19")
    virkning_fra: Optional[datetime] = Field(
        None,
        alias="virkningFra",
        description="EAID_AB768062_FD24_4960_8AA1_C6BFF90C00C5",
    )
    virkningsaktør: Optional[str] = Field(None, description="EAID_8E60197F_D857_47c6_8611_75B63D0940FD")
    virkning_til: Optional[datetime] = Field(
        None,
        alias="virkningTil",
        description="EAID_3058C5FD_9824_48ba_B62C_C24587BF6537",
    )
    navn: Optional[str] = Field(None, description="EAID_9E7FA46D_52D9_4615_B24C_599BB28D1923")
    postnr: Optional[str] = Field(None, description="EAID_8F8BACBF_E985_4dc1_BCF4_27F5C3FD0BB1")
    postnummerinddeling: Optional[str] = Field(None, description="EAID_E5F5DDF9_3CF4_4304_B02D_E67AB0CDD619")
