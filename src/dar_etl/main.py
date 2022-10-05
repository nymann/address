from pathlib import Path

import typer

from dar_etl.config import Config
from dar_etl.parsing.parser_factory import ParserFactory
from dar_etl.publisher import DarEntryPublisher

app = typer.Typer()


@app.command()
def main(json_file: Path) -> None:
    config = Config()
    publisher = DarEntryPublisher(host=config.kafka_host, port=config.kafka_port)
    count = 0
    for parser in ParserFactory.create_all():
        for entry in parser.parse(file_path=json_file):  # noqa: WPS519
            publisher.publish(dar_entry=entry, topic=parser.root_key)
            count += 1
    typer.echo(f"parsed {count} records")


if __name__ == "__main__":
    app()
