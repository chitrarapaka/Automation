class Solution:
    def findOnce(self,arr : list, n : int):
        for i in range(0,n-1,2):
            if arr[i] != arr[i+1]:
                return arr[i]
        return arr[n-1]
#{
Class Solution:
    def findonce(self,ar:list,n:int):
        for i in range(0,n-1,2):
            if arr[i]!=
