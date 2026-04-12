#!/usr/bin/env python3
"""
Ce module contient un générateur asynchrone qui produit des nombres aléatoires.
Il illustre l'utilisation de la boucle d'événements pour des attentes non-bloquantes.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Génère dix nombres aléatoires avec un intervalle d'une seconde entre chaque.

    La coroutine boucle dix fois. À chaque itération, elle suspend son
    exécution pendant une seconde de manière asynchrone avant de produire
    un nombre décimal aléatoire compris entre 0 et 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)