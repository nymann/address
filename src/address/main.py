from io import BufferedReader
from pathlib import Path
from typing import Type

from devtools import debug
import ijson
from pydantic import BaseModel
import typer

from address.dar_schemas.adresse import Adresse
from address.dar_schemas.adressepunkt import Adressepunkt
from address.dar_schemas.husnummer import Husnummer
from address.dar_schemas.navngiven_vej import NavngivenVej
from address.dar_schemas.navngiven_vej import NavngivenVejKommunedel
from address.dar_schemas.navngiven_vej import NavngivenVejPostnummer
from address.dar_schemas.navngiven_vej import NavngivenVejSupplerendeBynavn
from address.dar_schemas.navngiven_vej import Postnummer
from address.dar_schemas.supplerende_bynavn import SupplerendeBynavn

key_mapping: dict[str, Type[BaseModel]] = {
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

app = typer.Typer()


@app.command()
def main(data: Path) -> None:
    with open(file=data, mode="rb") as fp:
        read_keys(fp=fp)


def read_keys(fp: BufferedReader):
    for key, klass in key_mapping.items():
        read_key(fp=fp, key=key, klass=klass)


def read_key(fp: BufferedReader, key: str, klass: Type[BaseModel]) -> None:
    for record in ijson.items(fp, f"{key}.item"):
        debug(klass(**record))


if __name__ == "__main__":
    app()
