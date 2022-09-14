from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class Husnummer(BaseModel):
    """
    EAID_D0A626FC_CCAE_4209_B2F6_AC919B74A528
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
    adgangsadressebetegnelse: Optional[str] = Field(None, description="EAID_EDCC14FC_63ED_4ebe_8B52_3E406831A148")
    adgangspunkt: Optional[str] = Field(None, description="EAID_E3A37E0C_D0D8_4c30_BBD5_2F26F7A24591")
    husnummerretning: Optional[str] = Field(None, description="EAID_1A906922_EFAC_4182_AA8C_08332D52C6EE")
    husnummertekst: Optional[str] = Field(None, description="EAID_83A4C230_5C5A_4ffb_B136_0315DD9F8DBE")
    vejpunkt: Optional[str] = Field(None, description="EAID_F6BAEBD6_0306_4641_9DEA_C1441D986AFB")
    jordstykke: Optional[str] = Field(None, description="EAID_dst052F4B_D60C_4ccd_BAE5_6BCED78FE40C")
    placeret_på_foreløbigt_jordstykke: Optional[str] = Field(
        None,
        alias="placeretPåForeløbigtJordstykke",
        description="EAID_dstC82C82_CC9D_4d7d_9B8A_8F4A1ADFB5AE",
    )
    geo_danmark_bygning: Optional[str] = Field(
        None,
        alias="geoDanmarkBygning",
        description="EAID_dst3C28C5_D640_4bc0_9014_FDC7CBF30581",
    )
    adgang_til_bygning: Optional[str] = Field(
        None,
        alias="adgangTilBygning",
        description="EAID_dst3E4349_6115_4191_AF4F_243CCE561C41",
    )
    adgang_til_teknisk_anlæg: Optional[str] = Field(
        None,
        alias="adgangTilTekniskAnlæg",
        description="EAID_dst79A4C1_23B2_4c0c_85CC_60C6E2EA5AE0",
    )
    vejmidte: Optional[str] = Field(None, description="EAID_dstC9842D_CF82_4dc5_8114_3FF7AEF90C17")
    afstemningsområde: Optional[str] = Field(None, description="EAID_dstB6088D_EE9E_451c_8070_088AA4520FA6")
    kommuneinddeling: Optional[str] = Field(None, description="EAID_dst714AB4_FE21_446f_BEE5_7AE65691A45B")
    menighedsrådsafstemningsområde: Optional[str] = Field(
        None, description="EAID_dst08DF20_7055_4542_8D3D_F8FCCD9A7125"
    )
    sogneinddeling: Optional[str] = Field(None, description="EAID_dst0864F0_E380_4aa6_A644_25974107FC47")
    supplerende_bynavn: Optional[str] = Field(
        None,
        alias="supplerendeBynavn",
        description="EAID_dstF5C960_23DB_454c_A8A8_41B231DF61C7",
    )
    navngiven_vej: Optional[str] = Field(
        None,
        alias="navngivenVej",
        description="EAID_dst74C4B5_0F0F_4a51_B317_BA74938B605F",
    )
    postnummer: Optional[str] = Field(None, description="EAID_dst3F5BA7_EB6C_47a2_AC4B_90C72D4F3585")
