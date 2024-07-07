


def multi_level_selection_sort(arr, sort_keys):
    size = len(arr)

    for i in range(size - 1):
        min_index = i
        for j in range(i + 1, size):
            if compare_dicts(arr[j], arr[min_index], sort_keys):
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]


def compare_dicts(d1, d2, keys):
    for key in keys:
        if d1[key] < d2[key]:
            return True
        elif d1[key] > d2[key]:
            return False
    return False


if __name__ == "__main__":
    data = [
        {'First Name': 'Raj', 'Last Name': 'Nayyar'},
        {'First Name': 'Suraj', 'Last Name': 'Sharma'},
        {'First Name': 'Karan', 'Last Name': 'Kumar'},
        {'First Name': 'Raj', 'Last Name': 'Thakur'},
        {'First Name': 'Raj', 'Last Name': 'Sharma'},
        {'First Name': 'Kiran', 'Last Name': 'Kamla'},
        {'First Name': 'Armaan', 'Last Name': 'Kumar'},
        {'First Name': 'Jaya', 'Last Name': 'Sharma'},
        {'First Name': 'Ingrid', 'Last Name': 'Galore'},
        {'First Name': 'Jaya', 'Last Name': 'Seth'},
        {'First Name': 'Armaan', 'Last Name': 'Dadra'},
        {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
        {'First Name': 'Aahana', 'Last Name': 'Arora'},
        {'First Name': 'Banji', 'Last Name': 'Owabumoye'}
    ]

    sort_order = ['First Name', 'Last Name']
    multi_level_selection_sort(data, sort_order)

    for item in data:
        print(item)

# A simplified Syntax
def selection_sort(arr, keys):
    """
    Perform multi-level selection sort on a list of dictionaries.

    :param arr: List of dictionaries to be sorted.
    :param keys: List of keys to sort by, in order of preference.
    """
    size = len(arr)

    # Iterate through each element in the array
    for i in range(size - 1):
        min_index = i

        # Find the index of the minimum element based on the sorting keys
        for j in range(i + 1, size):
            for key in keys:
                if arr[j][key] < arr[min_index][key]:
                    min_index = j
                    break
                elif arr[j][key] > arr[min_index][key]:
                    break

        # Swap the found minimum element with the first element
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]


# Example usage
if __name__ == "__main__":
    # List of dictionaries to sort
    people = [
        {'First Name': 'Raj', 'Last Name': 'Nayyar'},
        {'First Name': 'Suraj', 'Last Name': 'Sharma'},
        {'First Name': 'Karan', 'Last Name': 'Kumar'},
        {'First Name': 'Raj', 'Last Name': 'Thakur'},
        {'First Name': 'Raj', 'Last Name': 'Sharma'},
        {'First Name': 'Kiran', 'Last Name': 'Kamla'},
        {'First Name': 'Armaan', 'Last Name': 'Kumar'},
        {'First Name': 'Jaya', 'Last Name': 'Sharma'},
        {'First Name': 'Ingrid', 'Last Name': 'Galore'},
        {'First Name': 'Jaya', 'Last Name': 'Seth'},
        {'First Name': 'Armaan', 'Last Name': 'Dadra'},
        {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
        {'First Name': 'Aahana', 'Last Name': 'Arora'},
        {'First Name': 'Banji', 'Last Name': 'Owabumoye'}
    ]

    # Define the sorting order
    sorting_order = ['First Name', 'Last Name']

    # Perform multi-level selection sort
    selection_sort(people, sorting_order)

    # Print the sorted list
    print(f"\n Second solution:\n")
    for person in people:
        print(f"{person}")
