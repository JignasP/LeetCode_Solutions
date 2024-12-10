#347. Top K Frequent Elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        nms={}
        for i in nums:
            if i in nms:
                nms[i] +=1
            else:
                nms[i]=1
                         
        nms=dict(sorted(nms.items(), key=lambda item: item[1],reverse=True))
        ls=list(nms.keys())
        return ls[:k:]
    
