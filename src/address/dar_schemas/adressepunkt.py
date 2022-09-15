from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class Adressepunkt(BaseModel):
    """
    EAID_00A7AF01_C512_4a85_ADB5_98FB15541948
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
    oprindelse_kilde: Optional[str] = Field(
        None,
        description="EAID_B9AAE6C5_974D_4d20_BABA_C62874774F4B.EAID_FD77FC95_714B_4779_B7FA_F9BBAB41758D",
    )
    oprindelse_nøjagtighedsklasse: Optional[str] = Field(
        None,
        description="EAID_B9AAE6C5_974D_4d20_BABA_C62874774F4B.EAID_B8A27494_DF27_4aa9_B1F4_EBD68D2479A5",
    )
    oprindelse_registrering: Optional[datetime] = Field(
        None,
        description="EAID_B9AAE6C5_974D_4d20_BABA_C62874774F4B.EAID_10DCC555_0BE9_4991_AD8C_DEA595CB08A0",
    )
    oprindelse_teknisk_standard: Optional[str] = Field(
        None,
        alias="oprindelse_tekniskStandard",
        description="EAID_B9AAE6C5_974D_4d20_BABA_C62874774F4B.EAID_181528AD_2DA3_4e9d_BF38_81916A924D2A",
    )
    position: Optional[str] = Field(None, description="EAID_4B062EDE_CE8C_414b_AB85_B5A1FD72AA78")
