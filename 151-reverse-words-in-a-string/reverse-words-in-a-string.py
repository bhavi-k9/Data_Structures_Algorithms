class Solution:
    def reverseWords(self, s: str) -> str:

        sl = s.split(" ")
        print(sl)

        so = []
        for i in range(len(sl)-1,-1,-1):
            if sl[i] != "":
                so.append(sl[i])

        print(so)    

        return " ".join(so)
        