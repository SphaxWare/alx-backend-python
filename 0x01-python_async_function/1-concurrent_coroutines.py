#!/usr/bin/env python3
"""Async"""
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """retunr list of delays"""
    delays = []
    sort = []
    for _ in range(n):
        delays.append(wait_random(max_delay))
    for delay in asyncio.as_completed(delays):
        result = await delay
        sort.append(result)
    return sort
