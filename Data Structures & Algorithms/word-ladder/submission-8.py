from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        def canTransform(begin, end):
            invalid = 0
            for i in range(len(begin)):
                if begin[i] != end[i]:
                    invalid += 1
            return invalid == 1

        q = deque([beginWord])
        visited = set()
        visited.add(beginWord)
        transformations = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return transformations
                for w in wordList:
                    if w in visited:
                        continue
                    if canTransform(word, w):
                        q.append(w)
                        visited.add(w)
            transformations += 1
        return 0
