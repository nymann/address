from typing import Optional

from pydantic import Field

from dar_etl.schemas.base_model import DarBaseModel


class SupplerendeBynavn(DarBaseModel):
    """
    EAID_9D39B21D_E73C_4f1b_9C6C_B75412DAAD77
    """

    navn: Optional[str] = Field(None, description="EAID_8359992A_59C4_48c4_981D_7A42F20CA168")
    supplerende_bynavn: Optional[str] = Field(
        None,
        alias="supplerendeBynavn",
        description="EAID_C6722E9B_EF6C_425d_9373_A933C01A6A64",
    )
