import collections


# 柠檬水找零
class SolutionA:
    def lemonadeChange(self, bills: list) -> bool:
        if not bills:
            return True
        remaining = {5: 0, 10: 0}
        for i in bills:
            if i == 5:
                remaining[5] += 1
            elif i == 10:
                remaining[5] -= 1
                remaining[10] += 1
            else:
                if remaining[10] >= 1:      # 有10的情况下优先找10
                    remaining[10] -= 1
                    remaining[5] -= 1
                else:
                    remaining[5] -= 3
            if remaining[5] < 0 or remaining[10] < 0:
                return False
        return True


# 买卖股票的最佳时机II
class SolutionB:
    def maxProfit(self, prices: list) -> int:
        if len(prices) <= 1:
            return 0
        start = prices[0]
        res = 0
        for i in prices[1:]:
            # 对紧跟谷的每一个峰值计算差并求和以最大化利润,
            # 如果跳过一个峰到下一个峰,中间一定会损失部分利润
            if i > start:
                res += (i - start)
                start = i
            else:
                start = i
        return res


# 分发饼干
class SolutionC:
    def findContentChildren(self, g: list, s: list) -> int:
        if not s or not g:
            return 0
        g.sort(reverse=True)        # 降序
        s.sort(reverse=True)        # 降序
        res = 0
        while g and s:              # gs均非空持续循环
            # 贪心,对每个胃口,选能满足的最小尺寸
            if g[-1] <= s[-1]:      # 满足胃口
                g.pop()
                s.pop()
                res += 1
            else:                   # 不满足胃口
                s.pop()
        return res


# 模拟行走机器人
class SolutionD:
    def robotSim(self, commands: list, obstacles: list) -> int:
        # 在前进方向分别为y轴正方向、x轴负方向、y轴负方向、x轴正方向时,x和y的变化规律
        # 方向[90, 180, 270, 360/0]度对应的坐标变换如下,列表从左向右代表左转,从右向左代表右转。
        diff = [(0, 1), (-1, 0), (0, -1), (1, 0)]

        # 初始坐标(x,y)以及转向的次数t
        x = y = t = 0
        dx, dy = 0, 1
        obstacleSet = set(map(tuple, obstacles))    # set数据类型类似dict执行in的数据复杂度为O(1)
        res = 0                                     # 坐标平方的最大值
        for cmd in commands:
            if cmd == -2:                           # turn left
                t = (t+1)%4
                dx, dy = diff[t][0], diff[t][1]
            elif cmd == -1:                         # turn right
                t = (t+3)%4
                dx, dy = diff[t][0], diff[t][1]
            else:
                for k in range(cmd+1):              # 前进cmd步长
                    if ((x+dx), (y+dy)) not in obstacleSet and k > 0:
                        x += dx
                        y += dy
                        res = max(res, x*x + y*y)
            print(x, y)
        return res


# 单词接龙
class SolutionE:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list) -> int:
        if endWord not in wordList:
            return 0
        wordmap = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(beginWord)):
                wordmap[word[:i]+"*"+word[i+1:]].append(word)
        deque = collections.deque([(beginWord, 1)])
        visited = {beginWord: True}
        while deque:
            current_word, level = deque.popleft()
            for i in range(len(beginWord)):
                t_word = current_word[:i] + "*" + current_word[i+1:]
                for word in wordmap[t_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        deque.append((word, level + 1))
                wordmap[t_word] = []
        return 0


# 岛屿数量
class SolutionF:
    def numIslands(self, grid: list) -> int:
        if len(grid) == 0:  # 边界条件
            return 0
        res, row, col = 0, len(grid), len(grid[0])

        for a in range(row):
            for b in range(col):  # 遍历所有节点
                stack = [(a, b)]
                if grid[a][b] == "1":  # 碰到节点值为1的点,res+1,并DFS进行整片"岛屿"置零
                    res += 1
                    grid[a][b] = "0"
                    while stack:
                        i, j = stack.pop()
                        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                            if 0 <= x < row and 0 <= y < col and grid[x][y] == "1":
                                stack.append((x, y))
                                grid[x][y] = "0"
        return res


# 扫雷游戏
class SolutionG:
    def updateBoard(self, board, click):
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        row, col = len(board), len(board[0])

        def tag(i, j):        # 计算ij周围的地雷数量更新ij的值,给当前点打标签
            c = 0
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1), (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]:
                if 0 <= x < row and 0 <= y < col:               # 注意这里x是第一维行,y是第二维列
                    if board[x][y] == "M":
                        c += 1
            board[i][j] = str(c) if c else "B"
        deque = collections.deque([(click[0], click[1])])       # deque的结构为[(), (), ()],初始化时记得元素队列外层加[]
        while deque:
            for _ in range(len(deque)):
                node = deque.popleft()
                i, j = node[0], node[1]
                tag(i, j)
                if board[i][j] in ["1", "2", "3", "4", "5", "6", "7", "8"]:  # 碰到数字终止这一层的遍历开始下一层遍历
                    continue
                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1), (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]:
                    if 0 <= x < row and 0 <= y < col:           # 注意这里x是第一维行,y是第二维列
                        if board[x][y] == "E":
                            deque.append((x, y))
                            # 注意这里要将xy置为"B"表示已经访问过,否则在ij周围遍历时会重复append到队列
                            board[x][y] = "B"
        return board


if __name__ == "__main__":
    pass
