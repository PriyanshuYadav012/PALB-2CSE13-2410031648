def smallest_subarray_length(x, arr):
    n = len(arr)
    min_len = n + 1
    current_sum = 0
    start = 0

    for end in range(n):
        current_sum += arr[end]

        while current_sum > x:
            min_len = min(min_len, end - start + 1)
            current_sum -= arr[start]
            start += 1

    if min_len == n + 1:
        return 0
    return min_len



if __name__ == "__main__":
    print(smallest_subarray_length(51, [1, 4, 45, 6, 0, 19]))  
    print(smallest_subarray_length(100, [1, 10, 5, 2, 7]))     