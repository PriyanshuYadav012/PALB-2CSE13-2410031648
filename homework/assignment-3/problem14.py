def find_duplicate(nums):

    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


if __name__ == "__main__":
    nums = list(map(int, input("Enter array elements: ").split()))
    result = find_duplicate(nums)
    print("Duplicate number is:", result)
