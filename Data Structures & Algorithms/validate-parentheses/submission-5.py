class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        par={'(':')', '[':']', '{':'}'}
        st=[]
        flag=False
        for i in s:
            if i in par:
                st.append(i)
                flag=True
            elif st:
                c=st[-1]
                if par[c]!=i:
                    return False
                else:
                    st.pop()
            else:
                return False
        if flag and len(st)==0:
            return True
        return False