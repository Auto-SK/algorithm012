class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        ans = []
        if (not nums or length < 3):
            return ans
        nums.sort()
        for k in range(length - 2):
            if (nums[k] > 0):
                return ans
            if (k > 0 and nums[k] == nums[k - 1]):
                continue
            l, r = k + 1, length - 1
            while (l < r):
                if (nums[k] + nums[l] + nums[r] == 0):
                    ans.append([nums[k], nums[l], nums[r]])
                    while (l < r and nums[l] == nums[l + 1]):
                        l += 1
                    while (l < r and nums[r] == nums[r - 1]):
                        r -= 1
                    l += 1
                    r -= 1
                elif (nums[k] + nums[l] + nums[r] < 0):
                    l += 1
                else:
                    r -= 1
        return ans