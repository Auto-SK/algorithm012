# 1. 将 nums 数组中每个元素的下标、值作为字典 dic 的值和键保存起来
# 2. 如果 target - key 在字典中，则返回两者的下标
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for val, key in enumerate(nums):
            if (target - key in dct):
                return [val, dct[target - key]]
            dct[key] = val