from typing import Union
from os import PathLike
from typing import Iterable
from typing import List
from collections.abc import Generator

WIN32: bool
LINUX: bool
DARWIN: bool
POSIX: bool
PY2: bool


def platform_data_dir() -> str:
    ...


def platform_config_dir() -> str:
    ...


def platform_cache_dir() -> str:
    ...


def get_app_data_dir(appname: str, *args) -> str:
    ...


def ensure_app_data_dir(appname: str, *args) -> str:
    ...


def get_app_config_dir(appname: str, *args) -> str:
    ...


def ensure_app_config_dir(appname: str, *args) -> str:
    ...


def get_app_cache_dir(appname: str, *args) -> str:
    ...


def ensure_app_cache_dir(appname: str, *args) -> str:
    ...


def find_exe(
    name: Union[str, PathLike],
    multi: bool = ...,
    path: Union[str, PathLike, Iterable[Union[str, PathLike]], None] = ...
) -> str | List[str] | None:
    ...


def find_path(name,
              path: Union[str, Iterable[Union[str, PathLike]]] = ...,
              exact: bool = ...) -> Generator[str, None, None]:
    ...