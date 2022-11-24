def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)
    
    d = [[0]*(m+1) for _ in range(n + 1)]
    
    # dp 테이블 초기화 (idx 0은 문자가 한개도 없다는 뜻이며 문자가 한개도 없는 경우 삽입과정을 거쳐야하기 때문에 문자 수만큼 cnt)
    for i in range(1, n + 1):
        d[i][0] = i
    for j in range(1, m + 1):
        d[0][j] = j
        
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = 1 + min(d[i][j - 1], d[i - 1][j], d[i - 1][j - 1])
    return d[n][m]

str1 = input()
str2 = input()

print(edit_dist(str1, str2))