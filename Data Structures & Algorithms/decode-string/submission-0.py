class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop()


                numstr = ""
                while stack and stack[-1].isdigit():
                    numstr = stack.pop()+numstr
                stack.append(int(numstr)*substr)

        return ''.join(stack)
        
        #time complexity = O(n)
        #space complexity = O(n)

        