from bisect import bisect_left, bisect_right

def countByRange(a, leftVal, rightVal):
    leftIdx = bisect_left(a, leftVal)
    rightIdx = bisect_right(a, rightVal)
    return rightIdx - leftIdx

arr = [[] for _ in range(10001)]
reArr = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    for word in words:
        arr[len(word)].append(word)
        reArr[len(word)].append(word[::-1])
    
    for i in range(10001):
        arr[i].sort()
        reArr[i].sort()
        
    for q in queries:
        if q[0] != '?':
            res = countByRange(arr[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            res = countByRange(reArr[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(res)
    return answer