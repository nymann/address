ARG DEBIAN_VERSION=bookworm

FROM nymann/debian-python3-dev:$DEBIAN_VERSION AS compile-image
COPY --chown=$USERNAME:$USERNAME . .
RUN apt-get update && \
    apt-get install --assume-yes --no-install-recommends lib && \
    rm -rf /var/lib/apt/lists/*
RUN make install

FROM nymann/debian-python3:$DEBIAN_VERSION AS production-image
USER $USERNAME
COPY --from=compile-image --chown=$USERNAME:$USERNAME "$VENV" "$VENV"
CMD dar_etl
