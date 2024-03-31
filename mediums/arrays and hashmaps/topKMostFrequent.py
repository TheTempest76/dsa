'''Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

 '''
from collections import Counter,defaultdict
class Solution:
    def topKFrequent(self, nums,k) :
        res = Counter(nums)
        sortedItems = sorted(res.items(),key = lambda x:x[1],reverse = True)
        list = [key for key , value in sortedItems[:k]]
        return list
    
sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3,3,3,3,4,4,1,4] ,3))