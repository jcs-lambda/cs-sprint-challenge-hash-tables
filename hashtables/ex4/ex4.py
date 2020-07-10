def has_negatives(a):
    """
    YOUR CODE HERE
    """
    a = sorted(a)

    ht = {}
    result = []

    for x in a:
        if x < 0:
            ht[abs(x)] = True
        elif x in ht:
            result.append(x)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
