def three_way_partition(arr, a, b):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] < a:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif a <= arr[mid] <= b:
            mid += 1
        else:  # arr[mid] > b
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return True

if __name__ == "__main__":
    arr1 = [1, 2, 3, 3, 4]

    arr2 = [1, 4, 3, 6, 2, 1]
    print(three_way_partition(arr2, 1, 3))  