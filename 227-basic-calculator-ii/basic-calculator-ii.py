class Solution:
    def calculate(self, s: str) -> int:
        # To ensure precedence we can build a list of ints and add them
        # We will be doing the multiplication and division before we push to the list
        # Implementation
        # loop over the string and count the number of digits until you encounter an operator or space
        # Upon encountering an operator if it's - push the negative of the digits after to the list
        # Upon encountering an operator if it's + push the digits after to the list
        # Upon encountering an operator if it's / or * perform the operation and then push the result
        s = s.replace(" ", "") # remove all spaces
        num = 0
        list1 = []
        sign = '+'
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(s[i])
            if not c.isdigit() or i == len(s)-1:
                if sign == '+':
                    list1.append(num)
                elif sign == '-':
                    list1.append(-num)
                elif sign == '/':
                    list1[-1] = int(list1[-1]/num)
                elif sign == '*':
                    list1[-1] *= num
                sign = c
                num = 0
                
            

        return sum(list1)
    
            
            
        