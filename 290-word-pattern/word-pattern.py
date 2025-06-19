class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        mapping = {}
        for i, (c, w) in enumerate(zip(pattern, words)):
            if mapping.get(('char', c), -1) != mapping.get(('word', w), -1):
                return False
            mapping[('char', c)] = mapping[('word', w)] = i
        return True
