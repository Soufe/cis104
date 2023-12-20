def kth_largest_element(arr, k):
    sorted_arr = sorted(arr, reverse=True)
    if 1 <= k <= len(sorted_arr):
        return sorted_arr[k - 1]
    else:
        return None