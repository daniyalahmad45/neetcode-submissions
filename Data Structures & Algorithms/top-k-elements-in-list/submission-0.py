class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = {}

        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        
        sort_dic = sorted(dic, key=dic.get, reverse=True)
        return sort_dic[:k]


