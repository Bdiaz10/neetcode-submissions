from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0
        if endWord not in wordList:
            return 0
        # adjlist of patterns -> words
        # {
        #   *at: [bat],
        #   c*t: []
        #   ca*: []
        # }
        graph = defaultdict(list)
        wordList.append(beginWord)
        for w in wordList:
            for i in range(len(w)):
                pattern = w[:i] + '*' + w[i+1:]
                graph[pattern].append(w)
        # BFS
        # pop from q and tansform to have a * at each index
        # add words that match the tranformation to the q
        q = deque()
        q.append((beginWord, 1))
        visited = set()
        visited.add(beginWord)
        while q:
            word, distance = q.popleft()
            if word == endWord:
                return distance
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                for w in graph[pattern]:
                    if w in visited:
                        continue
                    q.append((w, distance +1))
                    visited.add(w)
                graph[pattern] = []
        return 0   

