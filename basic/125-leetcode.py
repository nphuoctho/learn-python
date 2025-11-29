class Solution:
  def isPalindrome(self, s: str) -> bool:
    if not s: 
      return True
  
    result = []
    for c in s.lower():
      if c.isalnum():
        result.append(c)
    
    return result == result[::-1]
  

# Test Case
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
