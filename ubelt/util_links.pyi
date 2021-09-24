from typing import Union
from os import PathLike

FileExistsError = IOError


def symlink(real_path,
            link_path: Union[str, PathLike],
            overwrite: bool = ...,
            verbose: int = ...) -> str | PathLike:
    ...