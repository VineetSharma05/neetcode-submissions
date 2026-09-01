class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=set(['+','-','*','/'])
        st=[]
        for i in tokens:
            if i not in s:
                st.append(int(i))
            else:
                if i=='+':
                    e1=st.pop()
                    e2=st.pop()
                    st.append(e1+e2)
                elif i=='-':
                    e1=st.pop()
                    e2=st.pop()
                    st.append(e2-e1)
                elif i=='*':
                    e1=st.pop()
                    e2=st.pop()
                    st.append(e1*e2)
                else:
                    e1=st.pop()
                    e2=st.pop()
                    st.append(int(e2/e1))
        return st[0]
        