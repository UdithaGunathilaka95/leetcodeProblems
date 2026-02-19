# 1. Two Sum
def twoSum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j]+nums[i]==target:
              return [i,j]
                
print(twoSum([2,7,11,15], 9))

# 3. Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(s):
    sub = ""
    length = 0

    for i in range(len(s)):
        if s[i] not in sub:
            sub += s[i]
        else:
            index = sub.index(s[i])
            sub = sub[index + 1:] + s[i]
        if len(sub) > length:
            length = len(sub)
    return length

print(lengthOfLongestSubstring("adcdetfag"))

# 14. Longest Common Prefix
def longestCommonPrefix(strs):
    prefix = ""
    longestPrefix = ""
    boolean = True

    for i in range(len(strs[0])):
        prefix += strs[0][i]
        for word in strs:
            if not word.startswith(prefix):
                boolean = False
                break
        if boolean:
            longestPrefix = prefix
        else:
            break
    return longestPrefix
        

print(longestCommonPrefix(["flower","flow","flight"]))
  




        
                