

def common_elements(arr1, arr2, arr3):
    i = j = k = 0
    n1, n2, n3 = len(arr1), len(arr2), len(arr3)
    result = []
    while i < n1 and j < n2 and k < n3:
        if arr1[i] == arr2[j] == arr3[k]:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
            j += 1
            k += 1
        else:
            minimum = min(arr1[i], arr2[j], arr3[k])
            if arr1[i] == minimum:
                i += 1
            if arr2[j] == minimum:
                j += 1
            if arr3[k] == minimum:
                k += 1

    if not result:
        return [-1]

    return result
if __name__ == "__main__":
    arr1 = list(map(int, input("Enter elements of arr1: ").split()))
    arr2 = list(map(int, input("Enter elements of arr2: ").split()))
    arr3 = list(map(int, input("Enter elements of arr3: ").split()))

    result = common_elements(arr1, arr2, arr3)
    print(result)