
def dfs(nums :list[int], target : int, i : int, j : int) -> int:
    if i > j:
        return -1
    mid = (i + j) // 2
    if nums[mid] < target:
        return dfs(nums, target, mid + 1, j)
    elif nums[mid] > target:
        return dfs(nums, target, i, mid - 1)
    else:
        return mid


def binary_search(nums: list[int], target: int) -> int:
    """二分查找"""
    n = len(nums)
    # 求解问题 f(0, n-1)
    return dfs(nums, target, 0, n - 1)