def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2

    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        return binary_search_recursive(numbers_list, number_to_find, mid_index + 1, right_index)

    else:
        return binary_search_recursive(numbers_list, number_to_find, left_index, mid_index - 1)


if __name__ == "__main__":
    numbers_list = [1, 4, 6, 9, 10, 5, 7]
    number_to_find = 5

    # Sort the list programmatically
    numbers_list = sorted(numbers_list)

    indx = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list) - 1)
    print(f"The number '{number_to_find}' found at index {indx} using binary search")


def binary_search(list_e, target, left_idx, right_idx, idx_count=None):
    if idx_count is None:
        idx_count = []

    if left_idx > right_idx:
        return idx_count

    mid_idx = (left_idx + right_idx) // 2
    mid_num = list_e[mid_idx]

    if mid_num == target:
        idx_count.append(mid_idx)

        # Check for other occurrences to the left
        binary_search(list_e, target, left_idx, mid_idx - 1, idx_count)
        # Check for other occurrences to the right
        binary_search(list_e, target, mid_idx + 1, right_idx, idx_count)

    elif mid_num < target:
        binary_search(list_e, target, mid_idx + 1, right_idx, idx_count)
    else:
        binary_search(list_e, target, left_idx, mid_idx - 1, idx_count)

    return idx_count


if __name__ == "__main__":
    list_e = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    target = 15

    indices = binary_search(list_e, target, 0, len(list_e) - 1)
    print(f"The number '{target}' found at indices {indices} using binary search")
