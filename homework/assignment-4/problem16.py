

def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])

    merged = []
    current = intervals[0]

    for i in range(1, len(intervals)):
        if intervals[i][0] <= current[1]:
            current[1] = max(current[1], intervals[i][1])
        else:
            merged.append(current)
            current = intervals[i]

    merged.append(current)
    return merged


if __name__ == "__main__":
    n = int(input("Enter number of intervals: "))
    intervals = []

    print("Enter intervals (start end):")
    for _ in range(n):
        start, end = map(int, input().split())
        intervals.append([start, end])

    result = merge_intervals(intervals)
    print("Merged intervals:", result)