#!/usr/bin/env python3
"""
Module that provides a simple pagination server.
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start and end index for a given pagination configuration.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Gets the appropriate page of the dataset.

        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows corresponding to the page, 
            or an empty list if out of bounds.
        """
        # Le videur brutal : on vérifie que ce sont bien des entiers strictements positifs
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        # On calcule les index avec ta fonction précédente
        start, end = index_range(page, page_size)
        
        # On charge les données
        data = self.dataset()

        # Si l'index de départ dépasse la taille de la liste, on renvoie rien
        if start >= len(data):
            return []

        # Sinon on coupe la liste (le slicing gère tout seul la fin si 'end' est trop grand)
        return data[start:end]