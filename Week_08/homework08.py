# 有效的字母异位词
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


# 合并区间
class SolutionB:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged




