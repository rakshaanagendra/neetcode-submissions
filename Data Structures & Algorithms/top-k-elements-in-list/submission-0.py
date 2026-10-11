class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            count[num]=count.get(num,0)+1

        freq_buckets=[[] for _ in range(len(nums) +1)]

        for num, frequency in count.items():
            freq_buckets[frequency].append(num)
        
        result=[]
        for i in range(len(freq_buckets) -1, 0, -1):
            for num in freq_buckets[i]:
                result.append(num)
                if len(result)==k:
                    return result
