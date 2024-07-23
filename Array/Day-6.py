class Solution:

    def findMinDiff(self, A,N,M):
        
        A.sort()
        min_diff = float('inf')
        
        for i in range(N - M + 1):
            current_diff = A[i + M - 1] - A[i]
            if current_diff < min_diff:
                min_diff = current_diff
        
        return min_diff

        # code here

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N= int(input())
        A = [int(x) for x in input().split()]
        N= int(input())
    
        solObj = Solution()
        print(solObj.findMinDiff(A,N,M))