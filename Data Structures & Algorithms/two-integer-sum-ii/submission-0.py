class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        list1=[]
        for i in range(0,len(numbers)):
            for j in range(i+1,len(numbers)-1):
                if numbers[i]+numbers[j]==target:
                    list1.append(numbers[i])
                    list1.append(numbers[j])
        return list1