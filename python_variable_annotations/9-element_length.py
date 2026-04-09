#!/usr/bin/env python3
"""
Ce module contient une fonction annotée qui calcule la longueur
des éléments d'un itérable.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Prend un itérable de séquences et renvoie une liste de tuples.
    Chaque tuple contient l'élément original et sa longueur.

    Args:
        lst (Iterable[Sequence]): Un objet itérable contenant des séquences.

    Returns:
        List[Tuple[Sequence, int]]: Une liste de tuples (élément, longueur).
    """
    return [(i, len(i)) for i in lst]