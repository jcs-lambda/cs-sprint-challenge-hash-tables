def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    ht = {}

    for i, x in enumerate(weights):
        difference = limit - x
        if difference in ht:
            return (i, ht[difference])
        else:
            ht[x] = i

    return None
