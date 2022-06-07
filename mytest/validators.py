from asyncio import iscoroutinefunction
from types import FunctionType
from typing import Any

from mytest import decorators


def is_spec(item: Any):
    return isinstance(item, FunctionType) and hasattr(
        item, decorators.SPEC_ATTR
    )


def is_async_spec(item: Any):
    return iscoroutinefunction(item) and hasattr(
        item, decorators.ASYNC_SPEC_ATTR
    )
