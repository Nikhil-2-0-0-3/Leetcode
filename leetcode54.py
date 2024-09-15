class Solution(object):
    def spiralOrder(self, m):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        top=0
        left=0
        bottom=len(m)-1
        right=len(m[0])-1
        res=[]
        while True:
            for i in range(left,right+1):
                res.append(m[top][i])
            top=top+1
            if top > bottom or left > right:
                break

            for i in range(top,bottom+1):
                res.append(m[i][right])
            right-=1
            if top > bottom or left >right:
                break

            for i in range(right,left-1,-1):
                res.append(m[bottom][i])
            bottom-=1
            if top>bottom or left>right:
                break

            for i in range(bottom,top-1,-1):
                res.append(m[i][left])
            left+=1
            if top>bottom or left>right:
                break
        return res

        
