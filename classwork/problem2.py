

def find_min_max(arr):
    if not arr:
        return None
    
    minimum = arr[0]
    maximum = arr[0]
    
    for num in arr:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
    
    return [minimum, maximum]


# Example usage
if __name__ == "__main__":
    arr = [1, 4, 3, 5, 8, 6]
    result = find_min_max(arr)
    print(result)