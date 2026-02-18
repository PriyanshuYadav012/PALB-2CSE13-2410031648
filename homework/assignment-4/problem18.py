

def factorial_digits(n):
    result = [1]

    for num in range(2, n + 1):
        carry = 0
        for i in range(len(result)):
            product = result[i] * num + carry
            result[i] = product % 10
            carry = product // 10

        while carry:
            result.append(carry % 10)
            carry //= 10

    return result[::-1]


if __name__ == "__main__":
    n = int(input("Enter value of n: "))
    print(factorial_digits(n))