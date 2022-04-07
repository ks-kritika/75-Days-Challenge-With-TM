class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        b=[]
        for i in matrix:
            for j in i:
                b.append(j)
        return target in b