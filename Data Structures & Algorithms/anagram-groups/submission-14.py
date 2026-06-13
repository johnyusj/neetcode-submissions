class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        length = len(strs)
        dimensional_array = []
        list_hashmap = [ {} for _ in range(length) ]
        duplicate_hashmap = {}
        for i in range(length):
            for c in strs[i]:
                if (list_hashmap[i].get(c) == None):
                    list_hashmap[i][c] = 1
                else:
                    list_hashmap[i][c] += 1
        
        
        for s in range(length):
            immutable_map = frozenset(list_hashmap[s].items())
            if (duplicate_hashmap.get(immutable_map) == None):
                duplicate_hashmap[immutable_map] = [strs[s]]
            else:
                duplicate_hashmap[immutable_map].append(strs[s])

        for _,arr in duplicate_hashmap.items():
            dimensional_array.append(arr)

        return dimensional_array
            
            
