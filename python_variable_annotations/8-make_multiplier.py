#!/usr/bin/env python3
"""
Ce module contient une fonction qui génère une fonction multiplicatrice.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Crée une fonction qui multiplie un nombre par le multiplicateur donné.

    Args:
        multiplier (float): Le multiplicateur à utiliser.

    Returns:
        Callable[[float], float]: Une fonction qui prend un float et renvoie
        le résultat de sa multiplication par le multiplicateur.
    """
    def multiplier_func(n: float) -> float:
        """
        Multiplie un nombre par le multiplicateur de la fonction parente.
        """
        return n * multiplier

    return multiplier_func