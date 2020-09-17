class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dub = set()
        for num in nums:
            if num in dub:
                return True
            else:
                dub.add(num)
        return False