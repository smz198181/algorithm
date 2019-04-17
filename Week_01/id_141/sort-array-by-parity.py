class Solution:
    def sortArrayByParity(self, A):
        singular = []
        double = []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                double.append(A[i])
            else:
                singular.append(A[i])
        return double + singular

s1 = Solution()
print(s1.sortArrayByParity([3,1,2,4]))
