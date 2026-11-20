class Solution:
	def subsetSums(self, arr):
		# code here
		output=[]
		n=len(arr)
		def solve(ind,curr_sum):
		    if ind==n:
		        output.append(curr_sum)
		        return
		    solve(ind+1,curr_sum+arr[ind])
		    solve(ind+1,curr_sum)
	    solve(0,0)
	    return output
	    
		