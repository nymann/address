from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class Adresse(BaseModel):
    """
    EAID_6043F4D9_C4CA_44d0_BE88_027166A8B008
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
    adressebetegnelse: Optional[str] = Field(None, description="EAID_BB398854_F92E_4372_A20A_D7136BB5CD9C")
    dørbetegnelse: Optional[str] = Field(None, description="EAID_16B39B2F_0D4D_45ca_8164_8E1D78D202FC")
    dørpunkt: Optional[str] = Field(None, description="EAID_2E77B0C3_49AF_47b0_AD4E_DD653B99FD0B")
    etagebetegnelse: Optional[str] = Field(None, description="EAID_805BB835_641D_49d5_93E6_80C8E3FFD91C")
    bygning: Optional[str] = Field(None, description="EAID_dst4A2C09_8035_4ca8_8AA0_CBAAB89AF135")
    husnummer: Optional[str] = Field(None, description="EAID_src6919CB_1734_44ef_BE5B_C115B637B2CD")
