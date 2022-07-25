import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)-1
        return [left if len(nums)!=left and nums[left]==target else -1, right if nums[right]==target else -1]