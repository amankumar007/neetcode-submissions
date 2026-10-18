class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h={}
        n=len(s)
        m=len(t)
        if m!=n:
            return False
        for i in range(m):
            if s[i] in h:
                h[s[i]]=h[s[i]]+1
            else:
                h[s[i]]=1
            if t[i] in h:
                 h[t[i]]=h[t[i]]-1
            else:
                h[t[i]]=-1
        if any([v for k,v in h.items() ]):
            return False
        return True

