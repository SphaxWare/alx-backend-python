#!/usr/bin/env python3
"""Async"""
import asyncio
import random


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    """retunr list of delays"""
    delays = []
    for _ in range(n):
        delay = wait_random(max_delay)
        delays.append(delay)
    return delays
