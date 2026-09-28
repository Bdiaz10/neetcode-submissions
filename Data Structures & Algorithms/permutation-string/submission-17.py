class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # is array with ord indx to store char frequencys

        # sliding window of size s1, updating the window freqs in the ord array
        # count the number of matches as the window moves to avoid (arr1 == arr2 calculations O(n))

        # when adding to a window, if the freqs match: increment matches
        # when removing from a window, if the freq is one less the s1freqs: decrement matches

        # remember to use ord indexing: ord(char) - ord('a')
        if len(s1) > len(s2):
            return False
        s1Freqs = [0] * 26
        window = [0] * 26
        for i, char in enumerate(s1):
            s1Freqs[ord(char)-ord('a')] +=1
            window[ord(s2[i])-ord('a')] +=1
        
        matches = 0
        for i in range(len(s1Freqs)):
            if s1Freqs[i] == window[i]:
                matches += 1
        
        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            idx = ord(s2[right])-ord('a')
            window[idx] += 1
            if window[idx] == s1Freqs[idx]:
                matches += 1
            elif window[idx] == s1Freqs[idx] +1:
                matches -= 1
            
            idx = ord(s2[left])-ord('a')
            window[idx] -= 1
            if window[idx] == s1Freqs[idx] -1:
                matches -= 1
            elif window[idx] == s1Freqs[idx]:
                matches += 1
            left += 1

        return matches == 26


