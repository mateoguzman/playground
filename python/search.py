

def find(nums: list[int], element: int):
    start = 0
    end = len(nums) - 1

    while start < end:
        middle = start + end // 2