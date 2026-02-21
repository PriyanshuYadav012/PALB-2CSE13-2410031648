

def is_palindrome(num):
    return str(num) == str(num)[::-1]


def all_palindromes(arr):
    for num in arr:
        if not is_palindrome(num):
            return False
    return True


# Example usage
if __name__ == "__main__":
    print(all_palindromes([111, 222, 333, 444, 555]))  
    print(all_palindromes([121, 131, 20]))             