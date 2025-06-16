class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode()
        n = len(s)
        for word in wordDict:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_end = True
        
        @lru_cache(None)
        def dfs(start):
            if start==n:
                return True
            node = root
            for i in range(start, n):
                ch = s[i]
                if ch not in node.children:
                    return False
                node = node.children[ch]
                if node.is_end and dfs(i+1):
                    return True
            return False
        
        return dfs(0)