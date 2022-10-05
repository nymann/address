from kafka import KafkaProducer

from dar_etl.schemas.base_model import DarBaseModel


class DarEntryPublisher:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

        self.producer = self._setup_connection()

    def publish(self, dar_entry: DarBaseModel, topic: str) -> None:
        encoded_dar_entry = dar_entry.json().encode("utf-8")
        self.producer.send(topic=topic, key=dar_entry.id_local, value=encoded_dar_entry)
        self.producer.flush()

    def _setup_connection(self) -> KafkaProducer:
        return KafkaProducer(bootstrap_servers=f"{self.host}:{self.port}")
