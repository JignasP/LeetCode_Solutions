#287. Find the Duplicate Number

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lst=set()
        for num in nums :

            if num in lst :
                return num

            else:
                lst.add(num)
