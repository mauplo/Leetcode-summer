class Solution(object):
    def isPalindrome(self, x):
       # We convert x into a string
       s = str(x)
      # We fill a deque with the characters in the string
       queue = deque()
       for char in s:
             queue.append(char)
      # We start popping in stack and queue manner, if the ends aren't the same, it's not a palindrome 
             if queue.popleft() != queue.pop():
                   return False
       return True
