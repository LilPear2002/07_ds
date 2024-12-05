
# 可以将列表视为动态数组

# 初始化列表
nums1 : list[int] = []
nums : list[int] = [1,3,2,5,4]

# 访问元素
num : int = nums[1]
# 更新元素
nums[1] = 6

# 插入与删除元素

# 清空列表
nums.clear()
# 添加元素
nums.append(1)
nums.append(3)
nums.append(2)
nums.append(5)
nums.append(4)

# 在中间插入元素
nums.insert(3, 6)

# 删除元素
nums.pop(3)

# 遍历列表
# 通过索引遍历
count = 0
for i in range(len(nums)):
    count += nums[i]

count = 0
# 直接遍历元素
for num in nums:
    count += num

# 拼接列表
nums1 : list[int] = [6,8,7,10,9]
nums += nums1

# 排序
nums.sort()

