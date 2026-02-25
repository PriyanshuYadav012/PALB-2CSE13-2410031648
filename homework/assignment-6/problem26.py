def find_median(arr):
    n = len(arr)
    
 
    arr.sort()

    if n % 2 != 0:
        return arr[n // 2]

    else:
        mid1 = arr[n // 2 - 1]
        mid2 = arr[n // 2]
        return (mid1 + mid2) / 2

print(find_median([90, 100, 78, 89, 67]))  
print(find_median([56, 67, 30, 79]))       
print(find_median([1, 2]))                 