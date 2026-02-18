def get_min_diff(arr, k):
    n = len(arr)
    
    if n == 1:
        return 0
    arr.sort()

    ans = arr[n - 1] - arr[0]

    small = arr[0] + k
    big = arr[n - 1] - k

    if small > big:
        small, big = big, small

    for i in range(1, n - 1):
        subtract = arr[i] - k
        add = arr[i] + k

        if subtract >= small or add <= big:
            continue

        if big - subtract <= add - small:
            small = subtract
        else:
            big = add

    return min(ans, big - small)


if __name__ == "__main__":
    arr = list(map(int, input("Enter tower heights: ").split()))
    k = int(input("Enter value of k: "))

    result = get_min_diff(arr, k)
    print("Minimum possible difference is:", result)
