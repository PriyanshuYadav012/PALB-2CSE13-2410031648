

def is_subset(a, b):
    freq = {}

    for num in a:
        freq[num] = freq.get(num, 0) + 1

    for num in b:
        if num not in freq or freq[num] == 0:
            return False
        freq[num] -= 1

    return True
if __name__ == "__main__":
    a = list(map(int, input("Enter elements of array a: ").split()))
    b = list(map(int, input("Enter elements of array b: ").split()))

    result = is_subset(a, b)
    print(str(result).lower())