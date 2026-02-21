def min_length_SubarraySum(arr,x):
    n = len(arr)
    min_length = float('inf')
    current_sum = 0
    start = 0

    for end in range(n):
        current_sum = current_sum + arr[end]
        while current_sum > x:
            min_length = min(min_length, end - start + 1)
            current_sum = current_sum - arr[start]
            start = start + 1
            if min_length == 1:
                return 1
            if min_length == float('inf'):

                return -1
    return min_length
   
    if __name__ == "__main__":
        arr = [2, 3, 1, 2, 4, 3]
        x = 7
        result = min_length_SubarraySum(arr, x)
        print("The minimum length of a subarray with sum greater than", x, "is:", result)

            
