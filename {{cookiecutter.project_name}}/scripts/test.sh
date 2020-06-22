#!/usr/bin/env bash

set -e
set -x

pipenv run pytest --cov=app --cov=tests --cov-report=term-missing --cov-report=xml --cov-config=setup.cfg ${@}
