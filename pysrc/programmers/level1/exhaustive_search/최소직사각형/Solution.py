class Solution:
    def solution(sizes):
        # 각각의 요소의 세로를 최대값으로 만든다.
        # 최대값끼리 비교하고 최소값끼리 비교
        # 최대값 중에서 최대값을 세로로 최소값 중에서 최소값을 가로로 만든다
        # 세로와 가로를 곱한 값을 반환
        h, v = [],[]
        
        for size in sizes:
            h.append(max(size))
            v.append(min(size))
        return max(h) * max(v)

        # 다른 사람 풀이
        # return max(max(x) for x in sizes) * max(min(x) for x in sizes)