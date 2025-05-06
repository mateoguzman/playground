

# simple for loop

for i in range(10):
    print(i)

# loop a list

fruits = [ 'banana', 'orange', 'apple']
for fruit in fruits:
    print(f"Current fruit is : {fruit}, with index: {fruits.index(fruit)}" )

# loop a list with index

for i in range(len(fruits)):
    print(f"Fruit: {fruits[i]}, index: {i}")

for i in range(1,6):
    print(i)

# Dicts

nums = [1,5,6,8]
dict_nums = { nums[i] : i for i in range(len(nums))}
print(dict_nums)