# Multiprocessing Array, Value

import multiprocessing


def calc_square(numbers, result):
    for idx, n in enumerate(numbers):
        result[idx] = (n * n)
    print(f"inside process {result}")


if __name__ == "__main__":
    numbers = [2, 3, 6]
    result = multiprocessing.Array('i', 3)  # i means datatype integer and the size is 3
    p = multiprocessing.Process(target=calc_square, args=(numbers, result))

    p.start()
    p.join()

    print(result[:])


# Multiprocessing Array, Value

def calc_square(numbers, result, v):
    v.value = 5.67
    for idx, n in enumerate(numbers):
        result[idx] = (n * n)
    print(f"inside process {result}")

if __name__ == "__main__":
    numbers = [2, 3, 5]
    result = multiprocessing.Array('i', 3)  # 'i' means datatype integer and the size is 3
    v = multiprocessing.Value('d', 0.0)  # 'd' is double variable inside memory with 0.0 value
    p = multiprocessing.Process(target=calc_square, args=(numbers, result, v))

    p.start()
    p.join()

    print(v.value)
