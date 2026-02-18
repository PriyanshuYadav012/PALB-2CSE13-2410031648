

def triplet_sum(arr, target):
    arr.sort()
    n = len(arr)

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == target:
                return True
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return False


if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    target = int(input("Enter target: "))

    result = triplet_sum(arr, target)
    print(str(result).lower())