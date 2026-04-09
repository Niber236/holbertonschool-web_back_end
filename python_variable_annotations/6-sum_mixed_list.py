#!/usr/bin/env python3
"""
Ce module fournit une fonction annotée pour calculer la somme d'une liste mixte.
La liste acceptée en argument peut contenir des entiers et des décimaux.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calcule la somme d'une liste contenant des nombres entiers et des floats.

    Args:
        mxd_lst (List[Union[int, float]]): Une liste de nombres (int ou float).

    Returns:
        float: La somme totale des éléments de la liste.
    """
    return float(sum(mxd_lst))