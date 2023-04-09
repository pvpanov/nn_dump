import asyncio
import concurrent.futures as cf
import logging
from typing import Iterable

logger_format = "%(asctime)s:%(threadName)s:%(message)s"
logging.basicConfig(format=logger_format, level=logging.INFO, datefmt="%H:%M:%S")


def nice_way_to_multithread(
    funs: list,
    args: list[Iterable],
    kwargs: list[dict],
    max_workers: int = 2,
):
    with cf.ThreadPoolExecutor(max_workers=max_workers) as exec:
        future_to_mapping = [exec.submit(fun, arg, kwarg) for fun, arg, kwarg in zip(funs, args, kwargs)]
        return cf.as_completed(future_to_mapping)
