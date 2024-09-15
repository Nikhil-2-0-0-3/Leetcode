class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res=[[0 for _ in range(n)] for _ in range(n)]
        top=0
        bottom=n-1
        left=0
        right=n-1
        count=1
        while True:
            for i in range(left,right+1):
                res[top][i]=count
                count+=1
            top=top+1
            if top>bottom or left>right:
                break

            for i in range(top,bottom+1):
                res[i][right]=count
                count+=1
            right-=1
            if top>bottom or left>right:
                break

            for i in range(right,left-1,-1):
                res[bottom][i]=count
                count+=1
            bottom-=1
            if top>bottom or left>right:
                break
            
            for i in range(bottom,top-1,-1):
                res[i][left]=count
                count+=1
            left+=1
            if top>bottom or left>right:
                break
        return res
            
            
            

        
