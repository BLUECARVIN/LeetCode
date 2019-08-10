class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    	if len(arr1) == 0:
    		return []
        label_times = [0 for i in range(1001)] # record how many times that a number appeared in arr1
        
        for i in range(len(arr1)):
            label_times[arr1[i]] += 1
        
        ans = []
        for i in range(len(arr2)):
            for j in range(label_times[arr2[i]]):
                ans.append(arr2[i])
                label_times[arr2[i]] -= 1
        
        for i in range(1001):
            if label_times[i] != 0:
                for j in range(label_times[i]):
                    ans.append(i)
        return ans
# ------------ 60ms, 13.9MB ---------- #