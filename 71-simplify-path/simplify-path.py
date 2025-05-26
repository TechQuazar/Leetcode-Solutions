class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        1. .. cancels the prev directory/file. Then it becomes /// or //, just make it /
        2. . just means curr, so remove it.
        3. convert // and /// to /
        4. Remove ending /
        3. whatever left, add / in between
        if we split by /
        /.../a/../b/c/../d/./
        ["","...",'b','d']
        """
        if path[-1] =='/':
            path = path[:len(path)-1]
        s = ""
        i=0
        while i<len(path):
            ch = path[i]
            s+=ch
            if ch=='/':
                while i+1<len(path) and path[i+1]=='/':
                    i+=1
            i+=1
        if s and s[-1]=='/':
            s = s[:len(s)-1]
        path = s
        print('path',path)
        parts = path.split('/')
        n = len(parts)
        i = 0
        final = []
        print('parts',parts)
        while i<n:
            if parts[i]=='..':
                if i-1>=0 and parts[i-1]!='' and final[-1]!="":
                    final.pop(-1)
                
                # prev is / root, so not possible to go up
                elif i-1>=0 and parts[i-1]=='':
                    pass
            elif parts[i]=='.':
                pass
            else:
                final.append(parts[i])

            i+=1
        print('final',final)
        res = '/'.join(final)
        return res if res!="" else "/"


