from os.path import basename


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    ht = {}

    for path in files:
        x = ht.setdefault(basename(path), [])
        x.append(path)
    
    result = []
    for query in queries:
        if query in ht:
            result += ht[query]

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
