ARG DEBIAN_VERSION=bookworm

FROM debian:$DEBIAN_VERSION as base-img
ENV USERNAME="normal"
ENV HOME="/home/$USERNAME"
ENV VENV="$HOME/.venv"
ENV PATH="$VENV/bin:$PATH"

RUN apt-get update && \
    apt-get install --assume-yes --no-install-recommends \
        libyajl2 \
        python3 && \
    rm -rf /var/lib/apt/lists/* && \
    useradd -m --shell /bin/bash -u 1000 $USERNAME

FROM base-img AS compile-image
RUN apt-get update && \
    apt-get install --assume-yes --no-install-recommends \
        python3-dev \
        gcc \
        g++ \
        pkg-config \
        make \
        git \
        python3-pip \
        python3-venv \
        libyajl-dev && \
    rm -rf /var/lib/apt/lists/*

USER $USERNAME
ENV APP_DIR="$HOME/app"
RUN mkdir "$APP_DIR"
WORKDIR "$APP_DIR"

RUN python3 -m venv $VENV && \
    pip install --upgrade pip setuptools wheel

COPY --chown=$USERNAME:$USERNAME . .
RUN make install

FROM base-img AS production-image
USER $USERNAME
COPY --from=compile-image --chown=$USERNAME:$USERNAME "$VENV" "$VENV"
CMD dar_etl
