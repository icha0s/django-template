#!/usr/bin/env bash

set -e
set -x


pipenv run flake8 app
#pipenv run mypy --show-error-codes app

pipenv run black --check app --diff --target-version py38
pipenv run isort --recursive --check-only app