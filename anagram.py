
# find if strings are anagrams of each other
# assume only letters and strings are same length
# Time complexity is O(n^2)
def isAnagramIterative(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    
    # same length
    if len1 != len2:
        return False;
    
    # check that each character in str1 is in str2
    # if not found then they are not anagrams
    for i in xrange(len1):
        isMatched = False
        for j in xrange(len2):
            if str1[i] == str2[j]:
                isMatched = True
                break;
        if(not isMatched):
            return False
    return True
    
# Check that each character in the first string is present in the second
# by checking off each character from the second string, if all characters
# are checked off then the strings are anagrams
# Time complexity is O(n^2)
def isAnagramWithCheckOff(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 != len2:
        return False
        
    s2List = list(s2)
    
    pos1 = 0
    stillOk = True
    while pos1 < len1 and stillOk:
        pos2 = 0
        found = False
        while pos2 < len2 and not found:
            if s1[pos1] == s2List[pos2]:
                found = True
            else:
                pos2 += 1
            
        if found:
            s2List[pos2] = None
        else:
            stillOk = False
        
        pos1 += 1
    
    return stillOk   
    
# The sorting algorithm dominates the times complexity ->
# depending on how it is implemented could be at worst O( n^2 )
# at best O(n log n )
def isAnagramBySorting(s1, s2):
    
    if (len(s1) != len(s2)):
        return False
        
    list1 = list(s1);
    list2 = list(s2);
    list1.sort()
    list2.sort()
    
    pos = 0
    matches = True
    len1 = len(s1)
    while pos < len1 and matches:
        if list1[pos] == list2[pos]:
            pos += 1
        else:
            matches = False
    return matches

# Time complexity O(n) -> by O(n + n + 26)
# Achievable by using additional storage to keep two list of character counts
# Sacrificing space to gain time
def isAnagramByHistogram(s1, s2):
    histogram1 = [0] * 26
    histogram2 = [0] * 26
    len1 = len(s1)
    len2 = len(s2)
    
    for i in range(len1):
        pos = ord(s1[i]) - ord('a')
        histogram1[pos] += 1
        
    for i in range(len2):
        pos = ord(s2[i]) - ord('a')
        histogram2[pos] += 1
        
    j = 0
    isMatched = True
    while j < 26 and isMatched:
        if histogram1[j] == histogram2[j]:
            j += 1
        else:
            isMatched = False
    
    return isMatched

def main():
    
    str1 = "heart"
    str2 = "earth"
    # str2 = "earths"
    
    result = isAnagramIterative(str1, str2)
    
    print("\"%s\" and \"%s\" are anagrams: %s\n" %(str1, str2, "true" if result else "false"))
    
    
    str1 = "python"
    str2 = "typpon"
    # str2 = "earths"
    
    result = isAnagramIterative(str1, str2)
    print("\"%s\" and \"%s\" are anagrams: %s\n" %(str1, str2, "true" if result else "false"))
    
    result = isAnagramWithCheckOff(str1, str2)
    print("checkoff:\n\"%s\" and \"%s\" are anagrams: %s\n" %(str1, str2, "true" if result else "false"))
    
    result = isAnagramBySorting(str1, str2)
    print("sorting:\n\"%s\" and \"%s\" are anagrams: %s\n" %(str1, str2, "true" if result else "false"))
    result = isAnagramByHistogram(str1, str2)
    print("Histogram:\n\"%s\" and \"%s\" are anagrams: %s\n" %(str1, str2, "true" if result else "false"))
    
    
    
    str1 = "aes"
    str2 = "a"
    result = isAnagramWithCheckOff(str1, str2)
    print("checkoff:\n\"%s\" and \"%s\" are anagrams: %s\n" %(str1, str2, "true" if result else "false"))
    result = isAnagramBySorting(str1, str2)
    print("sorting:\n\"%s\" and \"%s\" are anagrams: %s\n" %(str1, str2, "true" if result else "false"))
    result = isAnagramByHistogram(str1, str2)
    print("Histogram:\n\"%s\" and \"%s\" are anagrams: %s\n" %(str1, str2, "true" if result else "false"))
    
if __name__ == '__main__':
    main()