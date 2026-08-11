class Solution:

    def encode(self, strs: List[str]) -> str:
        s=''
        if strs==[]:
            return "empty"
        for i in range(len(strs)-1):
            s+=strs[i]+'||'
        s+=strs[-1]
        return s

    def decode(self, s: str) -> List[str]:
        if s=="empty":
            return []
        return s.split('||')
