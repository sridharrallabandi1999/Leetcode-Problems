class Solution(object):
    def totalFruit(self, fruits):
        l = 0
        r = 0
        maxlen=0
        map={}
        n=len(fruits)
        while (r<n):
            if fruits[r] in map:
                map[fruits[r]]+=1
            else:
                map[fruits[r]]=1
            
            while (len(map)>2):
                map[fruits[l]]-=1

                if map[fruits[l]]==0:
                    del map[fruits[l]]    
                l+=1

            if (len(map))<=2:
                maxlen=max(maxlen,(r-l+1))
                r+=1
        return maxlen
                
        
        """
        :type fruits: List[int]
        :rtype: int
        """
        