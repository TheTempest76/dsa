from collections import *
'''in the first way you use the list of characters that are not zero as an indicator for anagram, however in the second one you sort it then use the sorted string as the indicator or the key for each value '''
class Solution:
    def groupAnagrams(self,strs):
        res = defaultdict(list)
        for str in strs:
            count = [0]*26
            for c in str:
               count[ord(c)-ord('a')] +=1
            res[tuple(count)].append(str)
        return res.values()

def groupAnagra(strs):
        res = defaultdict(list)
        for str in strs:
            sortedword = ''.join(sorted(str))
            res[sortedword].append(str)
        return res