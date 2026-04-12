#!/usr/bin/env python3
"""
This module provides the task_wait_n function, which uses task_wait_random.
It demonstrates executing multiple asyncio tasks concurrently.
"""
import asyncio
from typing import List

# Importation de task_wait_random depuis le fichier de la tâche 3
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay.

    This function collects the results as they complete using as_completed,
    ensuring the returned list is sorted by the duration of the delays.

    Args:
        n (int): The number of tasks to spawn.
        max_delay (int): The maximum delay for each task.

    Returns:
        List[float]: A list of all delays in ascending order of completion.
    """
    # On crée une liste de n Tasks en appelant task_wait_random
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    
    delays = []
    
    # On utilise as_completed pour récupérer les résultats au fur et à mesure
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
        
    return delays