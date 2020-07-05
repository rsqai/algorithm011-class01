"""
第二周作业
"""
import collections


# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
class SolutionA:
    def isAnagram(self, s: str, t: str) -> bool:
        f_map = {}
        if len(s) != len(t):
            return False
        for i in s:     # 构建s的字母频率字典f_map
            if i in f_map:
                f_map[i] += 1
            else:
                f_map[i] = 1
        for i in t:     # f_map减去t的字母频率
            if i in f_map:
                f_map[i] -= 1
            else:
                return False
        for i in f_map.values():
            if i != 0:      # f_map的values全为0则t、s是字母异位词
                return False
        return True


# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
class SolutionB:
    def groupAnagrams(self, strs: list) -> list:
        res = collections.defaultdict(list)
        for ss in strs:
            f = [0]*26      # strs中单词的n_hot初始化表示
            for s in ss:    # 构建strs中单词的n_hot表示,字母异位词具有相同的n_hot表示
                f[ord(s)-ord("a")] += 1
            res[tuple(f)].append(ss)
        return list(res.values())


# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
class SolutionC:
    def twoSum(self, nums: list, target: int) -> list:
        hashmap = {}
        for i in range(len(nums)):
            if target-nums[i] in hashmap:
                return [hashmap[target-nums[i]], i]
            hashmap[nums[i]] = i


class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Node:
    """
    Definition for a Node.
    """
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# 给定一个二叉树，返回它的中序 遍历。
class SolutionD:
    def inorderTraversal(self, root: TreeNode) -> list:
        res = []

        def helper(root):
            if not root:
                return None
            helper(root.left)
            res.append(root.val)
            helper(root.right)
        helper(root)
        return res


# 给定一个二叉树，返回它的 前序 遍历。
class SolutionE:
    def preorderTraversal(self, root: TreeNode) -> list:
        res = []

        def helper(root):
            if not root:
                return None
            res.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        return res


# 给定一个 N 叉树，返回其节点值的后序遍历。
class SolutionF:
    def postorder(self, root: 'Node') -> list:
        res = []

        def helper(root):
            if not root:
                return None
            for child in root.children:
                helper(child)
            res.append(root.val)
        helper(root)
        return res


# 给定一个 N 叉树，返回其节点值的前序遍历。
class SolutionG:
    def preorder(self, root: 'Node') -> list:
        res = []

        def helper(root):
            if not root:
                return None
            res.append(root.val)
            for child in root.children:
                helper(child)
        helper(root)
        return res


# 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。
class SolutionH:
    def levelOrder(self, root: 'Node') -> list:
        res = []

        def helper(root, level):
            if not root:
                return None
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            for child in root.children:
                helper(child, level+1)
        helper(root, 0)
        return res


# 我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
class SolutionI:
    def nthUglyNumber(self, n: int) -> int:
        dp, a, b, c = [1]*n, 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = dp[a]*2, dp[b]*3, dp[c]*5
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2:
                a += 1
            if dp[i] == n3:
                b += 1
            if dp[i] == n5:
                c += 1
        return dp[-1]


# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        hashmap = {}
        nums.sort()
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
        # 如果只通过hashmap中的value排序构建新的交换键值对后的dict,会出现冲突
        # 因此构建一个元组列表,按照元组的第二个元素降序排列
        tmp = sorted(hashmap.items(), key=lambda hashmap: hashmap[1], reverse=True)
        res = []
        for x, y in tmp:
            res.append(x)
        return res[:k]


if __name__ == "__main__":
    pass

