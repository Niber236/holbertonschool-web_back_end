#!/usr/bin/env python3
"""
Ce module contient une coroutine qui mesure le temps d'exécution total
de quatre compréhensions asynchrones exécutées en parallèle.
"""
import asyncio
import time

# Importation de la coroutine de la tâche précédente
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Exécute async_comprehension quatre fois en parallèle et mesure
    le temps total écoulé.

    Returns:
        float: Le temps total d'exécution en secondes.
    """
    start_time = time.perf_counter()
    
    # asyncio.gather permet de lancer les 4 coroutines en même temps
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    
    end_time = time.perf_counter()
    return end_time - start_time