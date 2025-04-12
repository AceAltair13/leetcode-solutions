class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # TC: O(N * L^2)
        # SC: O(N)

        wordList = set(wordList)

        if endWord not in wordList:
            return 0
        
        queue = deque()
        queue.append((beginWord, 1))
        visited = set(beginWord)

        while queue:
            word, length = queue.popleft()
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + c + word[i + 1:]
                    if new_word == endWord:
                        return length + 1
                    if new_word in wordList and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, length + 1))
        
        return 0