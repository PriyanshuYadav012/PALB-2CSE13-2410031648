

def kth_smallest(arr, k):
    arr.sort()
    
    return arr[k - 1]

if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements separated by space: ").split()))
    k = int(input("Enter value of k: "))
    
    result = kth_smallest(arr, k)
    print(f"{k}th smallest element is: {result}")