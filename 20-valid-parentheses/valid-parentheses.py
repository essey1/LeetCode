class Solution:
    def isValid(self, s: str) -> bool:
        """
        Input: s = "([])"
        check the inner [] and remove it then the outer is easy
        utilize a stack for LIFO
        1st itr = open bracket, append to stack check next
        2nd itr = open bracket, append to stack, check next
        3rd itr = closed bracket, check if 2nd itr is of same type? 
                Yes, pop the 2nd itr from the stack
                No, return false
            4th itr = closed bracket, check stack[-1], do they match?
                Yes I pop
                No, return false
            return true
        """

        stack = []
        hashs = {'}':'{', ']':'[', ')':'('}

        for c in s:
            if c == '{' or c == '[' or c == '(':
                stack.append(c)
            else:
                if not stack or hashs[c] != stack[-1]:
                    return False
                else:
                    stack.pop()
        if stack:
            return False
        return True