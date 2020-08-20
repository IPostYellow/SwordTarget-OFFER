'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？
'''
class Solution:#40ms,13.5MB
    def uniquePaths(self, m, n):
        f=[]
        tmp=[]
        for i in range(n):
            tmp.append(1)
        for j in range(m):
            f.append(tmp)
        for i in range(1,m):
            for j in range(1,n):
                f[i][j]=f[i-1][j]+f[i][j-1]
        return f[m-1][n-1]

S=Solution()
print(S.uniquePaths(3,2))

#java 0ms,36.2MB
# class Solution {
#     public int uniquePaths(int m, int n) {
#         int [][] f=new int[m][n];
#         for(int i=0;i<m;i++) f[i][0]=1;
#         for(int i=0;i<n;i++) f[0][i]=1;
#         for(int i=1;i<m;i++){
#             for(int j=1;j<n;j++)
#                 f[i][j]=f[i-1][j]+f[i][j-1];
#         }
#         return f[m-1][n-1];
#     }
# }