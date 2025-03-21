class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        '''
        recipe -> ingredients
        BRUTE FORCE
        for r in receipe
        can you create r based on its ingredients i => create(r)
        for each i, do you have it in suppy?
        if not, can you create it if it is a recipe create(r)? [cache useful]
        '''
        n = len(recipes)
        m = len(supplies)


        supplies = set(supplies)
        allRecipes = set(recipes)
        cache = {}
        res = []
        recipeToIdx = {}
        for i,r in enumerate(recipes):
            recipeToIdx[r] = i

        def canCreate(idx, seen):
            # print('idx,recipes',idx, recipes[idx])
            if idx in cache:
                return cache[idx]
            counter = 0
            for ing in ingredients[idx]:
                if ing in supplies:
                    counter+=1
                elif ing in allRecipes and ing not in seen:
                    # print('idx',idx,'ing',ing,'recipe',recipes[idx])
                    seen.add(ing)
                    if canCreate(recipeToIdx[ing],seen):
                        counter+=1
                    seen.remove(ing)
            isPossible = counter==len(ingredients[idx])
            cache[idx] = isPossible
            return isPossible

        for i,r in enumerate(recipes):
            seen = set()
            if canCreate(i,seen):
                cache[r] = True
                res.append(r)

        return res