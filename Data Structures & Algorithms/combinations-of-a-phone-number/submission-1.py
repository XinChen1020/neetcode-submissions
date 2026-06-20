class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        results = []
        stack = deque([[0, ""]])
        digits_mapping = {"2": "abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"}

        while stack:
            print(stack)
            idx, path = stack.pop()

            if idx == len(digits):
                results.append(path)
                continue

            for letter in digits_mapping[digits[idx]]:
                next_path = path
                next_path += letter
                stack.append([idx + 1, next_path])
        
        return results
