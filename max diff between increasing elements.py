ans=-1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    temp=nums[j]-nums[i]
                    ans=max(ans,temp)
        return ans