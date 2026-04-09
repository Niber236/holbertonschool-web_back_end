#!/usr/bin/env python3
"""
Ce module contient une fonction annotée qui transforme une chaîne
et un nombre en un tuple contenant la clé et le carré du nombre.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Prend une chaîne k et un nombre v (int ou float) et renvoie un tuple.
    Le premier élément est k, le second est le carré de v (annoté en float).

    Args:
        k (str): La chaîne de caractères.
        v (Union[int, float]): Le nombre à élever au carré.

    Returns:
        Tuple[str, float]: Un tuple (k, v^2).
    """
    return (k, v**2)