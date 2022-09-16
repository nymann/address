from pathlib import Path

import typer

from dar_etl.parsing.parser_factory import ParserFactory

app = typer.Typer()


@app.command()
def main(data: Path) -> None:
    count = 0
    for parser in ParserFactory.create_all():
        for item in parser.parse(file_path=data):
            count += 1
    typer.echo(f"parsed {count} records")


if __name__ == "__main__":
    app()
