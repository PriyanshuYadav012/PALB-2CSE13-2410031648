

def rotate_clockwise_by_one(arr):
    if len(arr) <= 1:
        return arr

    last_element = arr[-1]

    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = last_element

    return arr

arr = [1, 2, 3, 4, 5]
rotated_arr = rotate_clockwise_by_one(arr)
print(rotated_arr)