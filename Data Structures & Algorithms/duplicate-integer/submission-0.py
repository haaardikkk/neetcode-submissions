class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
   
        original = len(nums)
        modi = set(nums)
        modiLen = len(modi)

        if original == modiLen:
            return False
        else:
            return True