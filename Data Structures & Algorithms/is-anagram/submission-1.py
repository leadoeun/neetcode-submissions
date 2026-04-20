class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sdict = {}
        for c in s:
            if sdict.get(c):
                sdict[c] += 1
            else:
                sdict[c] = 1
        tdict = {}
        for c in t:
            if tdict.get(c):
                tdict[c] += 1
            else:
                tdict[c] = 1
        if len(sdict) != len(tdict):
            return False
        for k,v in sdict.items():
            if not tdict.get(k) or tdict[k] != v:
                return False
        return True