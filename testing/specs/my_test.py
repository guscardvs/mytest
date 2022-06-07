import mytest

def does_sum(*vals: int):
    return sum(vals)

@mytest.spec
def sum_returns_valid_result():
    assert does_sum(1, 1) == 2


@mytest.async_spec
async def sum_returns_zero_without_args():
    assert does_sum() == 0
