class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # try all the letter one by one
        # and check if the letter is same for all

        n = len(strs[0])
        out = []

        for j in range(n):
            current_char = strs[0][j]
            for i in range(len(strs)):
                
                if j >= len(strs[i]) or strs[i][j] != current_char:
                    return ''.join(out)
            
            out.append(current_char)

        return ''.join(out)

            