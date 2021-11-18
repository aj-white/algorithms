from typing import List, Optional, Union


def binary_search(items: List, target: Union[int, str]) -> Optional[int]:
    # Establish first and last indexes of items list
    first = 0
    last = len(items) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if items[midpoint] == target:
            return midpoint
        elif items[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None


def verify(index: int) -> str:
    if index is not None:
        print(f"Target found at index {index}")
    else:
        print("Target is not in list")


# Check with integers
numbers = [*range(1, 20)]
# Integer in the list
search_result = binary_search(numbers, 8)
verify(search_result)
# Integer not in the list
search_result = binary_search(numbers, 21)
verify(search_result)


# Check with strings
names = ["Jeff", "Toby", "Jemima", "Helen", "Jodi"]
# Binary search requires a sorted list
sorted_names = sorted(names)
# String in the list
search_result = binary_search(sorted_names, "Toby")
verify(search_result)
# String not in the list
search_result = binary_search(sorted_names, "Harry")
verify(search_result)
