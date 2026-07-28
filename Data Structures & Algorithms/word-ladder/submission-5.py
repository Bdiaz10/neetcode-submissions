from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def canTransform(begin, end):
            invalid = 0
            for i in range(len(begin)):
                if begin[i] != end[i]:
                    invalid += 1
            return invalid == 1

        print(canTransform('mist', 'miss'))
        # bfs
        # q starts with begin workd
        # pop q, if end word, count transformations
        #   if not, and next transformable words from wordlist to the q
        q = deque([beginWord])
        visited = set()
        transformations = 1
        while q:
            print(visited, q)
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return transformations
                visited.add(word)
                for w in wordList:
                    if w in visited:
                        continue
                    if canTransform(word, w):
                        q.append(w)
            transformations += 1

        return 0
