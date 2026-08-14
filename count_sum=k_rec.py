class Solution:
	def perfectSum(self, arr, target):
		# code here
		dp={}
		def solve(ind,total):
		    if ind==len(arr):
		        if total==target:
		            return 1
		        return 0
		    if total>target:
		        return 0
		    if (ind, total) in dp:
                return dp[(ind, total)]

            pick=solve(ind+1,total+arr[ind])

            not_pick=solve(ind+1,total)

            dp[(ind, total)] = pick + not_pick


            return dp[(ind, total)]


		return solve(0,0)
