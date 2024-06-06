#!/usr/bin/env python3
"""to_kv function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """to_kv function"""
    return (k, float(v ** 2))
