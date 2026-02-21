

def min_swaps_to_group_k(arr, k):
    n = len(arr)

    
    count = 0
    for num in arr:
        if num <= k:
            count += 1

   
    if count == 0 or count == n:
        return 0

   
    bad = 0
    for i in range(count):
        if arr[i] > k:
            bad += 1

    min_swaps = bad

    
    for i in range(1, n - count + 1):
        
        if arr[i - 1] > k:
            bad -= 1
 
        if arr[i + count - 1] > k:
            bad += 1

        min_swaps = min(min_swaps, bad)

    return min_swaps



if __name__ == "__main__":
    print(min_swaps_to_group_k([2, 1, 5, 6, 3], 3))           
    print(min_swaps_to_group_k([2, 7, 9, 5, 8, 7, 4], 6))      
    print(min_swaps_to_group_k([2, 4, 5, 3, 6, 1, 8], 6))      