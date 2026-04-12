#!/usr/bin/env python3
"""
Ce module contient une routine asynchrone qui exécute plusieurs coroutines
simultanément et renvoie la liste de leurs délais par ordre de complétion.
"""
import asyncio
from typing import List

# Importation de wait_random depuis le fichier précédent
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Exécute wait_random n fois avec le délai max_delay spécifié.

    Grâce à l'utilisation de asyncio.as_completed, les délais sont récupérés
    dans l'ordre où ils se terminent, garantissant une liste triée de manière
    ascendante sans appel explicite à une fonction de tri.

    Args:
        n (int): Le nombre de fois que wait_random doit être appelé.
        max_delay (int): Le délai maximum pour chaque appel.

    Returns:
        List[float]: La liste de tous les délais (valeurs float) générés.
    """
    # Création d'une liste de n tâches (coroutines)
    tasks = [wait_random(max_delay) for _ in range(n)]
    
    delays = []
    
    # asyncio.as_completed renvoie un itérateur qui donne les résultats
    # dès qu'une coroutine a fini son exécution.
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
        
    return delays