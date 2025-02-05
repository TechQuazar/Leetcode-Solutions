class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        a1 = [c for c in s1]
        a2 = [c for c in s2]
        indices = []
        for i in range(len(s1)):
            if a1[i]!=a2[i]:
                indices.append(i)
        # check a1
        for i in range(len(indices)-1):
            for j in range(i+1,len(indices)):
                a1[indices[i]],a1[indices[j]] = a1[indices[j]],a1[indices[i]]
                if ''.join(a1)==s2:
                    return True
                a1[indices[i]],a1[indices[j]] = a1[indices[j]],a1[indices[i]]
        
        # check a2
        for i in range(len(indices)-1):
            for j in range(i+1,len(indices)):
                a2[indices[i]],a2[indices[j]] = a2[indices[j]],a2[indices[i]]
                if ''.join(a2)==s1:
                    return True
                a2[indices[i]],a2[indices[j]] = a2[indices[j]],a2[indices[i]]

        return False