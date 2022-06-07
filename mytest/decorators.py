import typing

T = typing.TypeVar('T')
P = typing.ParamSpec('P')

SPEC_ATTR = '__mytest_spec__'
ASYNC_SPEC_ATTR = '__mytest_async_spec__'


def spec(func: typing.Callable[P, T]) -> typing.Callable[P, T]:
    func.__mytest_spec__ = True
    return func


def async_spec(
    func: typing.Callable[P, typing.Coroutine[typing.Any, typing.Any, T]]
) -> typing.Callable[P, typing.Coroutine[typing.Any, typing.Any, T]]:
    func.__mytest_async_spec__ = True
    return func
