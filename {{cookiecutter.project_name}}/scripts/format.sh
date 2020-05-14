#!/usr/bin/env bash

set -e

pipenv run autoflake --recursive --remove-all-unused-imports --remove-unused-variables --in-place app --exclude=__init__.py
pipenv run black app --target-version py38
pipenv run isort --recursive app