class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        '''
        Brute force - 
        i,j,k
        for each words[i] and words[j] - check if they are a part of words[k] -> if the count of them in words[k]>=2 then add words[k] to the result
        O n^3 solution
        repeated work
        Sorted would be better - based on length
        cat dog rat cats dogcatsdog catsdogcats ratcatdogcat hippopotamuses
        cache some work
        cats has cat, so cats[cat / index 0] = 1
        similarly dogcatsdog has dog and cat -> dogcatsdog[cat/0] = 1, dogcatsdog[dog/1] = 2
        -----------\U0001f446 DOGSHIT SOLUTION DO BETTER------------------------------
        RE: https://chatgpt.com/g/g-p-679e3f2312cc8191a7f4c1563bcba423-lc-and-oa/c/67dc3a84-d374-800f-a9a5-0422026eb0f1
        Brute force - looked up one line for idea \U0001f622
        trying to split each word into 2 or more parts
        for word in words:
            for i in range(1,len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in dict AND (suffix in dict OR recur(suffix) # can be split into other valid parts):
                    add word to res
        ------------------\U0001f446 MANY suffix are checked repeatedly, just memoize it---------------------
        '''
        wordSet = set(words)
        cache = {}
        res = []
        words.sort(key=lambda x:-len(x))
        def canFormWord(word):
            if word in cache:
                return cache[word]
            n = len(word)
            for i in range(1,n):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in wordSet:
                    if suffix in wordSet or canFormWord(suffix):
                        cache[word] = True
                        return True
            cache[word] = False
            return False

        for word in words:
            if not word:
                continue
            wordSet.remove(word) # to avoid it being compared against itself
            if canFormWord(word):
                res.append(word)
            wordSet.add(word)
        return res

                    
