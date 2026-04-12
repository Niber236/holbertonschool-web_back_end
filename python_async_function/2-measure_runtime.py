#!/usr/bin/env python3
"""
Ce module contient une fonction qui mesure le temps d'exécution
moyen de la routine asynchrone wait_n.
"""
import time
import asyncio

# Importation de wait_n depuis le fichier spécifié
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Mesure le temps d'exécution total de wait_n(n, max_delay)
    et renvoie le temps moyen par itération (temps total / n).

    Args:
        n (int) : Le nombre de coroutines à lancer.
        max_delay (int) : Le délai maximum par coroutine.

    Returns:
        float : Le temps moyen écoulé pour chaque tâche.
    """
    start_time = time.time()  # Début de la mesure [cite : prompt]
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()    # Fin de la mesure
    
    total_time = end_time - start_time
    return total_time / n     # Retourne le temps moyen [cite : prompt]