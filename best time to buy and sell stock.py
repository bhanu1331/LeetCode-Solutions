minval=prices[0]
        ans=0
        for i in range(1,len(prices)):
                ans=max(ans,prices[i]-minval)
                minval=min(minval,prices[i])
        return ans