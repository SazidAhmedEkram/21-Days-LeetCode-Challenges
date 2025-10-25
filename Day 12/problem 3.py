class Solution(object):
    def groupAnagrams(self, strs):
        sol = {}
        for i in strs:
            sort = "".join(sorted(i))
            if sort not in sol:
                sol[sort] = []
            sol[sort].append(i)
        return sol.values()