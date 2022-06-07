import traceback
from types import FunctionType
import typing

from mytest.validators import is_async_spec, is_spec

FuncFiles = typing.Generator[
    typing.Generator[FunctionType, None, None], None, None
]


async def run_functions(func_files: FuncFiles):
    for file in func_files:
        for func in file:
            try:
                await _run_func(func)
            except AssertionError as error:
                traceback.print_tb(error.__traceback__)


async def _run_func(func: typing.Callable):
    print('Running test: ', func.__name__)
    if is_async_spec(func):
        await func()
    if is_spec(func):
        func()
