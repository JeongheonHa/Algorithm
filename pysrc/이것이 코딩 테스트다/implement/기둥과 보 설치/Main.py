# build_frame 대로 하나씩 넣어보면서 가능한지 여부 확인
# 작업을 수행한 결과가 조건을 만족하지 않는다면 해당 작업은 무시되므로 순서대로 넣으며 기둥이나 보를 넣는 족족 조건에 만족해야한다.
# 추가 또는 삭제 해본 결과가 조건에 만족하는지 확인
# 가능하면 q에 추가 불가능 하면 q에서 제거
# 남은 것들을 x를 기준으로 정렬

def isPossible(q):
    for x, y, kind in q:
        if kind == 0:
            if y == 0 or [x-1, y, 1] in q or [x, y, 1] in q or [x, y-1, 0] in q:
                continue
            return False
        if kind == 1:
            if [x, y-1, 0] in q or [x+1, y-1, 0] in q or ([x-1, y, 1] in q and [x+1, y, 1] in q):
                continue
            return False
    return True # for 문이 끝나 모든 q를 확인 했을 때 문제가 없으면 True
            
            
def solution(n, build_frame):
    q = []
    for frame in build_frame:
        x, y, kind, option = frame
        if option == 0:
            q.remove([x, y, kind])
            if not isPossible(q):
                q.append([x, y, kind])
        if option == 1:
            q.append([x, y, kind])
            if not isPossible(q):
                q.remove([x, y, kind])
    return sorted(q)
            