class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        most_frequent = []
        for i in nums:
            if hashmap.get(i) == None:
                hashmap[i] = 1
            else: 
                hashmap[i] += 1
        
        sorted_by_value = dict(sorted(hashmap.items(), key=lambda hashmap: hashmap[1]))
        l = 0
        for i in reversed(sorted_by_value):
            if( l < k):
                most_frequent.append(i)
                l += 1
            else:
                break

        return most_frequent
            
