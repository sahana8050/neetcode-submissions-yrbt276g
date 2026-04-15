class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        strs.sort()
        first=strs[0]
        last=strs[-1]
        for i in range(len(first)):
            if i<len(last)and first[i]==last[i]:
                res=res+first[i]
            else:
                break
        return res