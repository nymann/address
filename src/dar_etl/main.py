from pathlib import Path

from devtools import debug
import typer

from dar_etl.parsing.parser_factory import ParserFactory
from dar_etl.schemas.root_keys import Root

app = typer.Typer()


@app.command()
def main(data: Path) -> None:
    postal_code_parser = ParserFactory.create(root_key=Root.postal_codes)
    fp = open(file=data, mode="rb")
    for postal_code in postal_code_parser.parse(file_pointer=fp):
        debug(postal_code)
    fp.close()


if __name__ == "__main__":
    app()
