class Solution:
    def solution(array, commands):
        return [sorted(array[a[0]-1:a[1]]).pop(a[2]-1) for a in commands]
    
        # 다른 사람 풀이
        return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))