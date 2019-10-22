# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(N * log(N) + N * m), where N folder length, m is average size of string
# Space Complexity: O(N * m)
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=lambda f: len(f))
        seen = set()

        for path in folder:
            for i in range(2, len(path)):
                if path[i] == '/' and path[:i] in seen:
                    break
            else:
                seen.add(path)

        return list(seen)


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
print(solution.removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]))
print(solution.removeSubfolders(["/a", "/a/b/c", "/a/b/d"]))
print(solution.removeSubfolders(["/a/b/c", "/a/b/ca", "/a/b/d"]))
