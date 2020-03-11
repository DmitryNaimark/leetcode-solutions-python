# https://leetcode.com/problems/alien-dictionary/
# ---------------------------------------------------
from typing import List
from collections import deque

# Runtime Complexity: O(V + E), since it's a Khan algorithm. V - vertices, E - edges.
# Space Complexity: O(?)
# Idea:
#       1. Initialize map {char: set of chars, which follow after char}.
#       2. Initialize degree map {ch: number of edges that go into(before) current ch} with zeros.
#       3. Fill in the map and degree map by comparing word[i][j] with word[i + 1][j] until letters are not the same.
#       4. Append all the vertices, which don't have any edges coming into them(degree[ch] == 0) to the queue.
#       5. Add poped node to result. For each neighbor of poped node, decrease degree by 1. If degree becomes 0, add it to q.
#       6. If result contains less chars than total amount of different chars, then there is a cycle in the graph - return ''.
#       7. Otherwise return already generated result.
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        result = ''
        if not words:
            return result

        # ch: set of chars - which letters follow *immediately* after letter ch
        map = {}

        # ch: int - how many letters go into(before) ch in this DAG (Directed Acyclic Graph)
        degree = {}

        # Set initial degree for each letter to 0
        for word in words:
            for ch in word:
                degree[ch] = 0

        for i in range(len(words) - 1):
            cur = words[i]
            next = words[i + 1]

            min_len = min(len(cur), len(next))
            for j in range(min_len):
                c1, c2 = cur[j], next[j]

                if c1 != c2:
                    # Initialize set for ch if it wasn't initialized earlier
                    if c1 not in map:
                        map[c1] = set()

                    if c2 not in map[c1]:
                        map[c1].add(c2)
                        degree[c2] += 1

                    break

        q = deque()
        for ch, count in degree.items():
            if count == 0:
                q.append(ch)

        while q:
            ch = q.popleft()
            result += ch

            if ch in map:
                for ch2 in map[ch]:
                    degree[ch2] -= 1
                    if degree[ch2] == 0:
                        q.append(ch2)

        # If there is a cycle, our result will contain less chars than total chars count.
        if len(result) < len(degree):
            return ''

        return result


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# "wertf"
print(solution.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))
# "zx"
print(solution.alienOrder(["z", "x"]))
# "" - order is invalid
print(solution.alienOrder(["z", "x", "z"]))
