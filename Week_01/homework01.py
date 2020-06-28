"""
第一周作业,按顺序
"""


# removeDuplicates删除排序数组中的重复项
class SolutionA:
    def removeDuplicates(self, nums: list) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i+1


# rotate旋转数组
class SolutionB:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        count = 0
        for i in range(0, len(nums)):
            if count == len(nums):
                break
            current = i
            prev = nums[i]
            while True:
                next = (current + k) % len(nums)
                prev, nums[next], current = nums[next], prev, next
                count += 1
                if i == current:
                    break


# mergeTwoLists合并两个有序链表
class SolutionC:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


# merge合并两个有序数组
class SolutionD:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        while j < n:
            if i >= m + j:
                nums1[i:i + n - j] = nums2[j:n]
                break
            if nums1[i] < nums2[j]:
                i += 1
            else:
                nums1[i], nums1[i + 1:] = nums2[j], nums1[i:len(nums1) - 1]
                j += 1
                i += 1


# twoSum两数之和
class SolutionE:
    def twoSum(self, nums: list, target: int) -> list:
        dic = {}
        for index, value in enumerate(nums):
            if target-value in dic:
                return [dic[target-value], index]
            dic[value] = index


# moveZeros移动零
class SolutionF:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                if i != j:
                    nums[i] = 0
                j += 1


# plusOne加一
class SolutionG:
    def plusOne(self, digits: list) -> list:
        i = 1
        digits[-i] = (digits[-i] + 1) % 10
        while not digits[-i]:
            i += 1
            if i <= len(digits):
                digits[-i] = (digits[-i] + 1) % 10
            else:
                digits.insert(0, 1)
                break
        return digits


# MyCircularDeque设计循环双端队列
class MyCircularDeque:
    def __init__(self, k: int):
        import collections
        self.q = collections.deque(maxlen=k)

    def insertFront(self, value: int) -> bool:
        return len(self.q) < self.q.maxlen and (self.q.appendleft(value) or True)

    def insertLast(self, value: int) -> bool:
        return len(self.q) < self.q.maxlen and (self.q.append(value) or True)

    def deleteFront(self) -> bool:
        return self.q and (self.q.popleft() or True)

    def deleteLast(self) -> bool:
        return self.q and (self.q.pop() or True)

    def getFront(self) -> int:
        return not self.q and -1 or self.q[0]

    def getRear(self) -> int:
        return not self.q and -1 or self.q[-1]

    def isEmpty(self) -> bool:
        return not self.q

    def isFull(self) -> bool:
        return len(self.q) == self.q.maxlen


# 接雨水
class SolutionI:
    def trap(self, height: list) -> int:
        n = len(height)
        left, right = 0, n-1
        SUM, tmp, high = 0, 0, 1
        while left <= right:
            while left <= right and height[left]<high:
                SUM += height[left]
                left += 1
            while right >= left and height[right]<high:
                SUM += height[right]
                right -= 1
            high += 1
            tmp += right-left+1
        return tmp-SUM


if __name__ == "__main__":
    pass



