def union_arrays(a, b):
    
    union_set = set()
    
    for num in a:
        union_set.add(num)
    
    for num in b:
        union_set.add(num)
    
    return list(union_set)

if __name__ == "__main__":
    a = [1, 2, 3, 2, 1]
    b = [3, 2, 2, 3, 3, 2]
    result = union_arrays(a, b)
    print(sorted(result))  
