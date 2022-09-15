from io import BufferedReader
from typing import Iterable, Type

from devtools import debug
import ijson
from pydantic import BaseModel

from dar_etl.schemas.root_keys import Root


class DarParser:
    def __init__(self, root_key: Root, parsing_type: Type[BaseModel]) -> None:
        self.root_key = root_key
        self.parsing_type = parsing_type

    def parse(self, file_pointer: BufferedReader) -> Iterable[BaseModel]:
        for record in ijson.items(file_pointer, f"{self.root_key}.item"):
            debug(record)
            yield self.parsing_type(**record)
