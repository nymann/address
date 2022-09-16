from pathlib import Path

import typer

from dar_etl.parsing.parser_factory import ParserFactory

app = typer.Typer()


@app.command()
def main(json_file: Path) -> None:
    count = 0
    for parser in ParserFactory.create_all():
        for _ in parser.parse(file_path=json_file):  # noqa: WPS519
            count += 1
    typer.echo(f"parsed {count} records")


if __name__ == "__main__":
    app()
