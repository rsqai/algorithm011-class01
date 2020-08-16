import collections


# 实现Trie(前缀树)
class Trie(object):
    def __init__(self):
        self.root = {}
        self.end_of_word = "#"

    def insert(self, word):
        node = self.root
        for char in word:
            # 键char不存在时返回{}给node,否则返回对应的值,最终形成一个节点为dict类型的树形结构
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False  # 一旦char不存在于当前的键中就返回false
            node = node[char]  # 如果char存在于当前的所有键中,其对应的值node[char]赋值给node,它也是一个dict
        return self.end_of_word in node  # 最后查看是否有结束标志

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True  # 同search只是不用检查以"#"结束


# 朋友圈
# 递归DFS
class SolutionA:
    def findCircleNum(self, M: list[list[int]]) -> int:
        row, res, visited = len(M), 0, [0] * len(M)

        def dfs(M_, visited_, i_):
            # i_当前处理的人id, j表示其他人id,固定i_遍历j_ ,将未访问过且与i_有朋友关系的人标记为已访问
            for j in range(len(M_)):
                if M_[i_][j] == 1 and visited_[j] == 0:
                    visited_[j] = 1
                    dfs(M_, visited_, j)  # 对每一个j执行同样的操作(DFS), 将连通i_的全部置1

        for i in range(len(M)):
            if visited[i] == 0:
                dfs(M, visited, i)
                res += 1
        return res


# 迭代BFS
class SolutionB:
    def findCircleNum(self, M: list[list[int]]) -> int:
        row, res, visited = len(M), 0, [0] * len(M)

        def bfs(i_, visited_):
            deque = collections.deque([i_])
            while deque:
                # for _ in range(len(deque))这一句可以省去,因为这里不必区分压入弹出的层级概念,按顺序从上层到下层,从左到右进行遍历即可
                curr = deque.popleft()
                visited[curr] = 1
                for j in range(row):
                    if M[curr][j] == 1 and visited_[j] == 0:
                        deque.append(j)

        for i in range(row):
            if visited[i] == 0:
                bfs(i, visited)
                res += 1
        return res


# 并查集
class SolutionC:
    def findCircleNum(self, M: list[list[int]]) -> int:
        class UnionFind(object):
            def __init__(self, size):
                self.p = [i for i in range(size + 1)]
                self.num = size

            def find(self, x: int):
                # 路径压缩的并查集
                if self.p[x] != x:
                    self.p[x] = self.find(self.p[x])
                return self.p[x]

            def union(self, a: int, b: int):
                if self.find(a) != self.find(b):
                    self.p[self.find(a)] = self.p[self.find(b)]
                    self.num -= 1

        if len(M) == 1:
            return 1
        uf = UnionFind(len(M))
        for i in range(len(M)):
            for j in range(i + 1, len(M)):
                if M[i][j]:
                    uf.union(i, j)
        return uf.num


if __name__ == "__main__":
    pass
