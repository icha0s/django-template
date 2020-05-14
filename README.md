# django-template

[![Python Version](https://img.shields.io/badge/python-3.8-blue)](https://www.python.org/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![wemake.services](https://img.shields.io/badge/%20-wemake.services-green.svg?label=%20&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAK7OHOkAAAAbUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP%2F%2F%2F5TvxDIAAAAIdFJOUwAjRA8xXANAL%2Bv0SAAAADNJREFUGNNjYCAIOJjRBdBFWMkVQeGzcHAwksJnAPPZGOGAASzPzAEHEGVsLExQwE7YswCb7AFZSF3bbAAAAABJRU5ErkJggg%3D%3D)](https://wemake.services)


## Features

- Supports latest `python3.8+`
- [`wemake.services`](https://github.com/wemake-services/wemake-django-template/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot) with the help of [`@dependabot`](https://dependabot.com/)
- [`pipenv`](https://github.com/pypa/pipenv) for managing dependencies
- [`mypy`](https://mypy.readthedocs.io)
- [`pytest`](https://pytest.org/)
- [`flake8`](http://flake8.pycqa.org/en/latest/) and [`wemake-python-styleguide`](https://wemake-python-styleguide.readthedocs.io/en/latest/) for linting
- [`docker`](https://www.docker.com/) for development, testing, and production
- [`sphinx`](http://www.sphinx-doc.org/en/master/) for documentation
- [`Gitlab CI`](https://about.gitlab.com/gitlab-ci/) with full `build`, `test`, and `deploy` pipeline configured by default


## Installation

Firstly, you will need to install [dependencies](https://cookiecutter.readthedocs.io/en/latest/):

```bash
pip install cookiecutter
```

Then, create a project itself:

```bash
cookiecutter gh:onufrienkovi/django-template
```
