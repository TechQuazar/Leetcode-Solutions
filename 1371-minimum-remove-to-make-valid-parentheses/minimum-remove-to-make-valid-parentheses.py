class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        stack
        if closing before opening, remove it
        if opening, add to stack, when closing encountered remove from stack
        if stack empty, remove all closing
        remove all from stack
        '''
        st = []
        toDelete = set()
        for i,x in enumerate(s):
            if x=='(':
                st.append(i)
            elif x==')':
                if st:
                    st.pop(-1)
                else:
                    toDelete.add(i)
        for idx in st:
            toDelete.add(idx)

        res = ""
        for i,x in enumerate(s):
            if i in toDelete:
                continue
            res+=x
        return res
        