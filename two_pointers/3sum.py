from typing import List


class Solution:
    def threeSum(self, num: List[int]) -> List[List[int]]:
        res = []
        num.sort()
        for i , n in enumerate(num):
            if i>0 and n == num[i-1]    :
                continue
            l,r = i+1,len(num)-1
            while l<r:
                sum = n + num[l] + num[r]
                if sum<0:
                    l+=1
                elif sum > 0 :
                    r-=1
                else:
                    res.append([n,num[l] , num[r]])
                    l+=1
                    while l<r and num[l] == num[l-1]:
                        l+=1
        return res