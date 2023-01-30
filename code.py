class Solution:    
    def checkArithmeticSubarrays(self, nums, l, r):
        result = []
        for i,j in zip(l,r):
            subarr = sorted(nums[i:j+1])
            flag, diff = True, subarr[1]-subarr[0]
            for k in range(2,len(subarr)):
                if subarr[k]-subarr[k-1] != diff:
                    flag = False
                    break
            result.append(flag)
        return result



