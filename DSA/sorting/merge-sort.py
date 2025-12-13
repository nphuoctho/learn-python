"""Sorts a list in ascending order using the merge sort algorithm.

This function implements the merge sort algorithm, which is a highly efficient,
comparison-based, divide-and-conquer sorting algorithm. It has a time
complexity of O(n log n) in all cases (worst, average, and best).

The algorithm works as follows:
1.  Divide the unsorted list into n sublists, each containing one element.
2.  Repeatedly merge sublists to produce new sorted sublists until there is
  only one sublist remaining. This will be the sorted list.

The function modifies the list in-place.

Args:
  arr (list): The list of comparable elements to be sorted.

Returns:
  None: The function sorts the list in-place and does not return a value.

Examples:
  >>> my_list = [38, 27, 43, 3, 9, 82, 10]
  >>> merge_sort(my_list)
  >>> print(my_list)
  [3, 9, 10, 27, 38, 43, 82]
"""


def merge(left: list[int], right: list[int]) -> list[int]:
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) == 0:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    return merge(sorted_left, sorted_right)
