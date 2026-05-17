from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for s in strs:
            c = tuple(sorted(list(Counter(s).items())))

            seen[c].append(s)

        return list(seen.values())