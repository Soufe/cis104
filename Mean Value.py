def mean(*arr):
    if not arr:
        return None
    return sum(arr) / len(arr)