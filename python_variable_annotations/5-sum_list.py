#!/usr/bin/env python3
"""
Ce module fournit une fonction annotée pour calculer la somme d'une liste.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Prend une liste de nombres décimaux et renvoie leur somme.
    """
    return sum(input_list)