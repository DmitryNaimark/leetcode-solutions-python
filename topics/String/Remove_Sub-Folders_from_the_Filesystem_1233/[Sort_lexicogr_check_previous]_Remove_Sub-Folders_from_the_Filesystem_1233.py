# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(T * log(T) + T), where T is total chars in folder.
# T * log(T) to sort all strings alphabetically. + T(actually more like +2T) to compare strings.
# Space Complexity: O(N * m), m is average size of string.
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()

        res = []
        parent_size = 2
        # dummy value, so it will never find it's subchild
        parent = ' /'

        for path in folder:
            if path[:parent_size] != parent:
                res.append(path)
                # Adding slash means that we won't need to check cases like "/a/bc", "/a/bcd", because we make sure
                # that child has slash in the last position and it's compared with parent's slash, which we add here.
                parent = path + '/'
                parent_size = len(parent)

        return res


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
print(solution.removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]))
print(solution.removeSubfolders(["/a", "/a/b/c", "/a/b/d"]))
print(solution.removeSubfolders(["/a/b/c", "/a/b/ca", "/a/b/d"]))
