

def twoSum(nums: list[int], target: int):
    iterations = 0
    for i in nums:
        for j in nums:
            iterations += 1
            print(f"Iteration: {iterations}. Elements: {i}:{j}")
            #sum = i + j
            #if sum == target:
            #    return [nums.index(i),nums.index(j)]
    return [1,1]

def twoSum2(nums: list[int], target: int):
    iterations = 0
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            iterations += 1
            print(f"Iteration: {iterations}. Elements: {nums[i]}, {nums[j]}, Index: {i}:{j}")
            sum = nums[i] + nums[j]
            print(f"Sum: {sum}")
            if sum == target:
                print(f"Returning: {i}, {j}")
                return [i, j]

def twoSum3(nums: list[int], target: int):
    iterations = 0

    # nums = [2,3,6]
    # target = 5
    # nums_dict = { 2:0, 3:1, 6:2}
    #         


    # dictionary of nums
    nums_dict = { nums[i]: i for i in range (len(nums))}

    for i in range(0, len(nums)):
        print(f"Number: {nums[i]}")
        target_key = target - nums[i]
        print(f"Target number: {target_key}")
        if target_key > 0 and target_key in nums_dict and nums_dict[target_key] != i:
            return [i, nums_dict[target_key]]

def twoSum4(nums: list[int], target: int):
    iterations = 0

    # nums = [2,3,6]
    # target = 5
    # nums_dict = { 2:0, 3:1, 6:2}
    #         


    # dictionary of nums
    nums_dict = {}
    for i in range(len(nums)):
        num = nums[i]
        target_key = target - num
        if target_key in nums_dict and nums_dict[target_key] != i:
            return [i, nums_dict[target_key]]
        nums_dict[num] = i
    return [0,0]


# Test cases

target = 10
numbers = [ 2, 8, 10, 11, 15 ]
expected_result = [ 0, 1 ]
print(f"Test case 1.")
print(f"Numbers: {numbers}")
print(f"Target: {target}")

result = twoSum4(numbers,target)

if result == expected_result:
    print("PASS")
else:
    print(f"FAIL, expected {expected_result}, got {result}")

# TC2

target = 6
numbers = [ 3, 2,4 ]
expected_result = [ 1,2 ]
print(f"Test case 2.")
print(f"Numbers: {numbers}")
print(f"Target: {target}")

result = twoSum4(numbers,target)

if result == expected_result:
    print("PASS")
else:
    print(f"FAIL, expected {expected_result}, got {result}")


