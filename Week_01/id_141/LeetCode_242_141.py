class Solution:
    def isAnagram(self, s, t):
        hashS = {}
        for charNum in s:
            if charNum in hashS.keys():
                hashS[charNum] += 1
            else:
                hashS[charNum] = 1
        for charNum in t:
            if charNum not in hashS.keys():
                return False
            elif hashS[charNum] == 1:
                del hashS[charNum]
            else:
                hashS[charNum] -= 1;
        if len(hashS.keys()) != 0:
            return False
        return True
            
        
