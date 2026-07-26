class Solution:
    def frequencySort(self, s: str) -> str:
        my_dict=dict()
        for ch in s:
            my_dict[ch]=my_dict.get(ch,0)+1
        sorted_data = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
        ans=""
        for item,freq in sorted_data:
            ans+=item*freq
        return ans

        