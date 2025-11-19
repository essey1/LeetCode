class Solution:
    def isValid(self, s: str) -> bool:
        """
        We can solve this problem by using a stack
        If we encounter an opening bracket we can push it to stack
        If we encounter a closing bracet we can check the top of the stack
        If top is not opening bracket of same type:
            return false
        return true at the end if stack is empty which means all parenthesis are valid
        We can use a hashmap were the openning are key and closing are value
        """
        #Initialize
        stack = []
        pairs = {"{":"}", "[":"]", "(":")"}

        # loop and check by utilizing the stack
        for i in s:
            if i in pairs:
                stack.append(i)
            else:
                if not stack or pairs[stack[-1]] != i:
                    return False
                stack.pop()

        # Check if all parentheses are closed
        if len(stack) == 0:
            return True
        else:
            return False