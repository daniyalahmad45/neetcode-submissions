class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        matching = { "}" : "{",
                     "]" : "[",
                     ")" : "("}

        for char in s:
            if char not in matching:
                stack.append(char)
            else:
                if not stack:
                    return False
                if stack[-1] != matching[char]:
                    return False

                stack.pop()

        return len(stack) == 0



        
        