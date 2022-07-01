FROM python:3.10

ENV PYTHONUNBUFFERED=1

ARG WORKDIR=/wd
ARG USER=user

WORKDIR ${WORKDIR}

RUN useradd --system ${USER} && \
    chown --recursive ${USER} ${WORKDIR}

RUN apt update && apt upgrade -y

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install --requirement requirements.txt


COPY --chmod=755 ./docker/app/entrypoint.sh /entrypoint.sh
COPY --chmod=755 ./docker/app/start.sh /start.sh


COPY ./Makefile Makefile

COPY ./manage.py manage.py
COPY ./core ./core/
COPY ./apps ./apps/


USER ${USER}

ENTRYPOINT ["/entrypoint.sh"]

VOLUME ${WORKDIR}/db
EXPOSE 8000
