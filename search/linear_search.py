from typing import List, Optional, Union


def linear_search(items: List, target: Union[int, str]) -> Optional[int]:
    """Returns the index position of the target if found, else None"""
    for index, value in enumerate(items):
        if items[index] == target:
            return index
    return None


def verify(index: int) -> str:
    if index is not None:
        print(f"Target found at index {index}")
    else:
        print("Target is not in list")


numbers = [*range(1, 20)]
search_result = linear_search(numbers, 8)
verify(search_result)
search_result = linear_search(numbers, 21)
verify(search_result)
