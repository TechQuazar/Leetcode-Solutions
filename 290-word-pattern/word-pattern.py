class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        seen = defaultdict(str)
        seenWords = set()
        words = s.split()
        if len(pattern)!=len(words):
            return False
        for i,ch in enumerate(pattern):
            if ch in seen and seen[ch]!=words[i]:
                return False
            if ch not in seen and words[i] in seenWords:
                return False
            seen[ch] = words[i]
            seenWords.add(words[i])
        return True