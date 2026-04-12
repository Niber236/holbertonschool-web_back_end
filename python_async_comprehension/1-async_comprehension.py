#!/usr/bin/env python3
"""
Ce module contient une coroutine qui utilise une compréhension de liste asynchrone.
Il montre comment collecter efficacement les données d'un générateur asynchrone.
"""
from typing import List

# Importation dynamique de async_generator depuis la tâche précédente
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collecte 10 nombres aléatoires via une compréhension de liste asynchrone.

    Cette coroutine parcourt le générateur asynchrone et stocke chaque
    valeur produite dans une liste avant de la renvoyer.
    """
    return [i async for i in async_generator()]