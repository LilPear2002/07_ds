import random

# 初始化数组
arr : list[int] = [0] * 5
nums : list[int] = [1,2,3,4,5]

# 访问元素
def random_access(nums : list[int]) -> int:
    # 随机访问一个元素
    random_index = random.randint(0,len(nums) - 1)
    return nums[random_index]

# 在指定位置插入元素
def insert(nums : list[int], num : int, index : int):
    for i in range(len(nums) - 1, index , -1):
        nums[i] = nums[i - 1]

    nums[index] = num

# 删除指定位置的元素
def delete(nums : list[int], index : int):
    for i in range(index , len(nums) - 1):
        nums[i] = nums[i + 1]

# 遍历数组
def traverse(nums : list[int]):
    count = 0
    # 通过索引遍历
    for i in range(len(nums)):
        count += nums[i]
    # 直接遍历数组元素
    for num in nums:
        count += num
    # 同时遍历
    for i,num in enumerate(nums):
        count += nums[i]
        count += i

# 查找元素
def find(nums : list[int] , target : int) -> int:
    for i in range(len(nums)):
        if(nums[i] == target):
            return i
    return -1

# 扩容数组
def extend(nums : list[int], enlarge : int) -> list[int]:
    # 初始化一个扩容后的数组
    res = [0] * (len(nums) + enlarge)
    for i in range(len(nums)):
        res[i] = nums[i]
    return res
