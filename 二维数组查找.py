class Solution:
    def binarysearch(self, target, lists, left, right):
        mid = (left + right) // 2
        if target == lists[mid]:
            return True
        if left > right:
            return False
        if target < lists[mid]:
            return self.binarysearch(target, lists, left, mid - 1)
        if target > lists[mid]:
            return self.binarysearch(target, lists, mid + 1, right)

    def Find(self, target, array):
        for i in array:
            flag = self.binarysearch(target, i, 0, len(i)-1)
            if flag:
                return True
            else:
                continue
        return False


P = Solution()
target = 15
array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
print(P.Find(target, array))
