class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      max_length = 0
      start_index = 0
      seen = set()
            
      for i in range(len(s)):
        while s[i] in seen:
          seen.remove(s[start_index])
          start_index += 1
        
        seen.add(s[i])
        max_length = max(max_length, i - start_index + 1)
      
      return max_length
    
    
sol = Solution()
r = sol.lengthOfLongestSubstring("abcabcbb")
print(r)