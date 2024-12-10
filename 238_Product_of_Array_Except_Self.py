#238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:       

        if 0 not in nums:
            prod =math.prod(nums)
            lst=list(int(prod/nums[i]) for i in range(0,len(nums)))
            return(lst)       
        else:
            lst= list(int(math.prod(nums[0:i:]+nums[i+1::]))for i in range(0,len(nums)))
            return(lst)  
