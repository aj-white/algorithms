from typing import List, Union


def recursive_binary_search(items: List, target: Union[int, str]) -> bool:
    if not items:
        return False
    else:
        midpoint = len(items) // 2

        if items[midpoint] == target:
            return True
        else:
            if items[midpoint] < target:
                return recursive_binary_search(items[midpoint + 1 :], target)
            else:
                return recursive_binary_search(items[: midpoint - 1], target)


def verify(result):
    print(f"Target found: {result}")


# Verify with integers
numbers = [*range(10)]
# Integer in list
result = recursive_binary_search(numbers, 5)
verify(result)
# Integer not in list
result = recursive_binary_search(numbers, 12)
verify(result)

# Verify with strings
names = ["Jeff", "Toby", "Jemima", "Helen", "Jodi"]
# Binary search requires a sorted list
sorted_names = sorted(names)
# Name in list
result = recursive_binary_search(sorted_names, "Toby")
verify(result)
# Name not in list
result = recursive_binary_search(sorted_names, "Steve")
verify(result)
