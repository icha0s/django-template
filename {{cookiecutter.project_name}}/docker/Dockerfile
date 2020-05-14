FROM python:3.8.2-alpine3.11

RUN apk add --update build-base ca-certificates make
RUN apk add \
    libjpeg \
    zlib \
    zlib-dev \
    libwebp \
    openjpeg \
    jpeg-dev \
    postgresql-libs \
    postgresql-dev \
    openssh-client

WORKDIR /app
RUN pip install pipenv
RUN pipenv --three

COPY ./Pipfile ./Pipfile.lock ./Makefile /app/
RUN make req

EXPOSE 8000
