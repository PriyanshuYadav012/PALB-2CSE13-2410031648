

def kth_smallest(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return None
    
    arr.sort()    
    return arr[k - 1]

if __name__ == "__main__":
    arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
    k = 4
    result = kth_smallest(arr, k)
    print(result)