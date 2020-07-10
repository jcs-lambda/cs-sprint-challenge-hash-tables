def intersection(arrays):
    """
    YOUR CODE HERE
    """
    result = []

    seen = {}

    for array in arrays:
        for value in array:
            if value in seen and value not in result:
                result.append(value)
            else:
                seen[value] = True

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
