# https://leetcode.com/problems/longest-common-subsequence/
# ---------------------------------------------------


# Runtime Complexity: O(text1 * text2)
# Space Complexity: O(text1 * text2)
# Idea:
#     Compare two strings character by character.
#       - If chars are the same, increase subsequence length, skip both.
#       - If chars are not the same, try both cases: skip char in first string, skip char in second string.
#
#     Add Memoization:
#         If we have already calculated (i, j) and subsequence length was same or larger, don't calculate again.
class Solution:
    def __init__(self):
        self.longest_subseq = 0

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.longest_subseq = 0

        memo = {}
        self.lcs_recursively(text1, text2, 0, 0, 0, memo)

        return self.longest_subseq

    def lcs_recursively(self, s1, s2, i, j, subseq, memo):
        if i == len(s1) or j == len(s2):
            self.longest_subseq = max(subseq, self.longest_subseq)
            return

        if subseq <= memo.get((i, j), -1):
            return

        memo[(i, j)] = subseq
        if s1[i] == s2[j]:
            self.lcs_recursively(s1, s2, i + 1, j + 1, subseq + 1, memo)
        else:
            self.lcs_recursively(s1, s2, i + 1, j, subseq, memo)
            self.lcs_recursively(s1, s2, i, j + 1, subseq, memo)


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 3
print(solution.longestCommonSubsequence("abcde", "ace"))
# 3
print(solution.longestCommonSubsequence("abc", "abc"))
# 0
print(solution.longestCommonSubsequence("abc", "def"))
# (!) RecursionError: maximum recursion depth exceeded
print(solution.longestCommonSubsequence("fcvafurqjylclorwfoladwfqzkbebslwnmpmlkbezkxoncvwhstwzwpqxqtyxozkpgtgtsjobujezgrkvevklmludgtyrmjaxyputqbyxqvupojutsjwlwluzsbmvyxifqtglwvcnkfsfglwjwrmtyxmdgjifyjwrsnenuvsdedsbqdovwzsdghclcdexmtsbexwrszihcpibwpidixmpmxshwzmjgtadmtkxqfkrsdqjcrmxkbkfoncrcvoxuvcdytajgfwrcxivixanuzerebuzklyhezevonqdsrkzetsrgfgxibqpmfuxcrinetyzkvudghgrytsvwzkjulmhanankxqfihenuhmfsfkfepibkjmzybmlkzozmluvybyzsleludsxkpinizoraxonmhwtkfkhudizepyzijafqlepcbihofepmjqtgrsxorunshgpazovuhktatmlcfklafivivefyfubunszyvarcrkpsnglkduzaxqrerkvcnmrurkhkpargvcxefovwtapedaluhclmzynebczodwropwdenqxmrutuhehadyfspcpuxyzodifqdqzgbwhodcjonypyjwbwxepcpujerkrelunstebopkncdazexsbezmhynizsvarafwfmnclerafejgnizcbsrcvcnwrolofyzulcxaxqjqzunedidulspslebifinqrchyvapkzmzwbwjgbyrqhqpolwjijmzyduzerqnadapudmrazmzadstozytonuzarizszubkzkhenaxivytmjqjgvgzwpgxefatetoncjgjsdilmvgtgpgbibexwnexstipkjylalqnupexytkradwxmlmhsnmzuxcdkfkxyfgrmfqtajatgjctenqhkvyrgvapctqtyrufcdobibizihuhsrsterozotytubefutaxcjarknynetipehoduxyjstufwvkvwvwnuletybmrczgtmxctuny", "nohgdazargvalupetizezqpklktojqtqdivcpsfgjopaxwbkvujilqbclehulatshehmjqhyfkpcfwxovajkvankjkvevgdovazmbgtqfwvejczsnmbchkdibstklkxarwjqbqxwvixavkhylqvghqpifijohudenozotejoxavkfkzcdqnoxydynavwdylwhatslyrwlejwdwrmpevmtwpahatwlaxmjmdgrebmfyngdcbmbgjcvqpcbadujkxaxujudmbejcrevuvcdobolcbstifedcvmngnqhudixgzktcdqngxmruhcxqxypwhahobudelivgvynefkjqdyvalmvudcdivmhghqrelurodwdsvuzmjixgdexonwjczghalsjopixsrwjixuzmjgxydqnipelgrivkzkxgjchibgnqbknstspujwdydszohqjsfuzstyjgnwhsrebmlwzkzijgnmnczmrehspihspyfedabotwvwxwpspypctizyhcxypqzctwlspszonsrmnyvmhsvqtkbyhmhwjmvazaviruzqxmbczaxmtqjexmdudypovkjklynktahupanujylylgrajozobsbwpwtohkfsxeverqxylwdwtojoxydepybavwhgdehafurqtcxqhuhkdwxkdojipolctcvcrsvczcxedglgrejerqdgrsvsxgjodajatsnixutihwpivihadqdotsvyrkxehodybapwlsjexixgponcxifijchejoxgxebmbclczqvkfuzgxsbshqvgfcraxytaxeviryhexmvqjybizivyjanwxmpojgxgbyhcruvqpafwjslkbohqlknkdqjixsfsdurgbsvclmrcrcnulinqvcdqhcvwdaxgvafwravunurqvizqtozuxinytafopmhchmxsxgfanetmdcjalmrolejidylkjktunqhkxchyjmpkvsfgnybsjedmzkrkhwryzan"))