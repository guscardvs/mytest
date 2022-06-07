import importlib
from pathlib import Path
from types import FunctionType
import typing

from mytest.validators import is_async_spec, is_spec


def find_files(file_path: Path, pattern: str):
    def _make_finder_generator():
        f_path = Path(file_path).resolve()
        if f_path.is_file():
            yield from (f_path,)
            return
        yield from f_path.glob(pattern)

    return list(_make_finder_generator())


def _make_import(root: str, file: Path):
    _, file_vals = file.as_posix().split(root, 1)
    import_str = '.'.join(file_vals.split('/')).removesuffix('.py')
    return f'{root}{import_str}'


def _make_functions_file_generator(root: str, file: Path):
    mod = importlib.import_module(_make_import(root, file))
    for item in mod.__dict__.values():
        if not isinstance(item, FunctionType):
            continue
        if not is_spec(item) and not is_async_spec(item):
            continue
        yield item


def find_functions(root: str, files: typing.Sequence[Path]):
    for file in files:
        yield _make_functions_file_generator(root, file)
