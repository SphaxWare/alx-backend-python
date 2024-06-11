#!/usr/bin/env python3
"""Async Comprehension"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """async_generator"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
