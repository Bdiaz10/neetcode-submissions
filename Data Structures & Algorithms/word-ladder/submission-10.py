from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0
        
        def canTransform(start, end) -> bool:
            flag = False
            for i, char in enumerate(start):
                if char != end[i]:
                    if flag:
                        return False
                    flag = True
            return True
        
        q = deque()
        q.append(beginWord)
        visited = set()
        transformations = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                visited.add(word)
                if word == endWord:
                    return transformations
                for w in wordList:
                    if w in visited:
                        continue
                    if canTransform(word, w):
                        q.append(w)
            transformations += 1
        return 0