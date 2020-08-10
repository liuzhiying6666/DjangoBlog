class solution:
    def stastr(self,hay:str,nee:str):
        L,n = len(nee),len(hay)
        for str in range(n-L+1):
            if hay[str:str+L] == nee:
                print(str)
                return str
        print(-1)
        return -1
if __name__ == '__main__':
    solution().stastr(hay='leetcode',nee='co')

class solution1:
    def strstr(self,haystack:str,needle:str) -> int:
        L,n = len(needle),len(haystack)
        if L == 0:
            return 0
        