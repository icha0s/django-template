from typing import Callable

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import DelegatedFactory, Factory
from services.user import UserService


class Factories(DeclarativeContainer):
    """Factories."""

    user: Callable[..., UserService] = Factory(UserService)


class Service(DeclarativeContainer):
    """Services."""

    user: Callable[..., UserService] = Factory(
        Factories.user
    )
