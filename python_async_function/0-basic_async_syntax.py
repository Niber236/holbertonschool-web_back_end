#!/usr/bin/env python3
"""
This module provides an asynchronous coroutine that waits for a random delay.
It demonstrates the use of the asyncio and random modules in Python.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds (inclusive)
    and eventually return the float value representing the delay duration.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay