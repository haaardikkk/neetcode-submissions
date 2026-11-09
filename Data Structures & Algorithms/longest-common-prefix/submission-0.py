class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        rslt = ""
        base = strs[0]

        for i in range(0,len(base)):
            for word in strs[1:]:
                if i == len(word) or word[i] != base[i]:
                    return rslt
            rslt += base[i]
        return rslt