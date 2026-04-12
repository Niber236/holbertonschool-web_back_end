#!/usr/bin/env python3
"""
This module provides a function to create an asyncio Task from a coroutine.
It demonstrates how to wrap asynchronous coroutines into tasks for execution.
"""
import asyncio

# Importation dynamique de wait_random depuis le fichier précédent
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task that executes the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay passed to the wait_random coroutine.

    Returns:
        asyncio.Task: A task object wrapping the wait_random coroutine execution.
    """
    return asyncio.create_task(wait_random(max_delay))