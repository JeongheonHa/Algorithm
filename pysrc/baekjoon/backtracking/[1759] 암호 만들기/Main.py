def dfs(cnt, idx):
    if cnt == l:    # 암호가 완성 됐을 때
        vo, co = 0, 0
        for word in ans:
            if word in vowel:
                vo += 1
            else:
                co += 1
                
        if vo >= 1 and co >= 2:
            print("".join(ans))
            
        return 
    
    for i in range(idx, c):
        ans.append(words[i])
        dfs(cnt+1, i+1)   # 백 트래킹
        ans.pop()           # dfs가 끝날 때마다 원래의 상태로 초기화


l, c = map(int, input().split())
words = sorted(input().split())
vowel = ['a', 'e', 'i', 'o', 'u']
ans = []
dfs(0, 0)
