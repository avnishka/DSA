from functools import lru_cache
class Solution:
	def perfectSum(self, arr, target):
		# code here
		MOD=10**9+7
		@lru_cache(maxsize=None)
		def solve(ind,total):
		    if total>target :
		        return 0
		    if len(arr)==ind:
		        if total==target:
		            return 1
		        else:
		            return 0
		    
		    pick=solve(ind+1,total+arr[ind])
		    n_pick=solve(ind+1,total)
		    return (pick+n_pick)%MOD
	return solve(0,0)   