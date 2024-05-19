class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dp1=[0 for _ in range(len(arr))]
        dp2=[0 for _ in range(len(arr))]

        dp1[-1]=len(arr)
        temp1=[(arr[-1],len(arr)-1)]

        for i in range(len(arr)-2,-1,-1):
            while len(temp1)>0 and temp1[-1][0]>arr[i]:
                temp1.pop()
            
            dp1[i]=temp1[-1][1] if len(temp1)>0 else len(arr)
            temp1.append((arr[i],i))
        

        dp2[0]=-1
        temp2=[(arr[0],0)]
        for i in range(1,len(arr)):
            while len(temp2)>0 and temp2[-1][0]>=arr[i]:
                temp2.pop()
            
            dp2[i]=temp2[-1][1] if len(temp2)>0 else -1
            temp2.append((arr[i],i))
        
        summ=0
        for i in range(len(arr)):
            summ+=(arr[i]*(((i-dp2[i])*(dp1[i]-i))%1000000007))%1000000007
        
        return summ%1000000007

                