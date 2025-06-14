class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        for s in strs:
            key = [0 for _ in range(26)]
            for ch in s:
                key[ord(ch)-ord('a')]+=1
            freq[tuple(key)].append(s)
        
        return list(freq.values())