def next_gap(gap):
    if gap <= 1:
        return 0
    return (gap // 2) + (gap % 2)


def merge_without_extra_space(a, b):
    n = len(a)
    m = len(b)
    gap = n + m
    gap = next_gap(gap)

    while gap > 0:
        i = 0
        j = gap

        while j < (n + m):
            if j < n and a[i] > a[j]:
                a[i], a[j] = a[j], a[i]

            elif i < n and j >= n and a[i] > b[j - n]:
                a[i], b[j - n] = b[j - n], a[i]

            elif i >= n and b[i - n] > b[j - n]:
                b[i - n], b[j - n] = b[j - n], b[i - n]

            i += 1
            j += 1

        gap = next_gap(gap)


if __name__ == "__main__":
    a = list(map(int, input("Enter elements of array a: ").split()))
    b = list(map(int, input("Enter elements of array b: ").split()))

    merge_without_extra_space(a, b)

    print("a[] =", a)
    print("b[] =", b)
