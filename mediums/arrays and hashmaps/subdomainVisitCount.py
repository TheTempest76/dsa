from collections import defaultdict
from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = defaultdict(int)
        for s in cpdomains:
            num = int(s.split(" ")[0])
            d = str(s.split(" ")[1])
            subd = d.split(".")
            for i in range(len(subd)):
                res[".".join(subd[i:])] += num
        li = [f'{freq} {dom}' for dom,freq in res.items()]
        return li
sol = Solution()

print(sol.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))