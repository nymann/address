from pathlib import Path

from devtools import debug
import typer

from dar_etl.parsing.parser_factory import ParserFactory

app = typer.Typer()


@app.command()
def main(data: Path) -> None:
    with open(file=data, mode="rb") as fp:
        for parser in ParserFactory.create_all():
            typer.echo(parser.root_key)
            for item in parser.parse(file_pointer=fp):
                debug(item)


if __name__ == "__main__":
    app()
