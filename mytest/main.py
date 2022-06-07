import argparse
import asyncio
from typing import Sequence
from mytest.finders import find_files, find_functions
from mytest.runner import run_functions


def main(argv: Sequence[str] | None = None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', type=str)
    parser.add_argument(
        '--pattern',
        '-p',
        type=str,
        dest='pattern',
        default='test_*.py',
        action='store',
    )
    args = parser.parse_args(argv)
    files = find_files(args.filepath, args.pattern)
    functions = find_functions(args.filepath, files)
    asyncio.run(run_functions(functions))

    return 0
