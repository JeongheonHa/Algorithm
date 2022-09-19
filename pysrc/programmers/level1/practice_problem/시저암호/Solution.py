class Solution:
    # 해당 요소에서 첫 번째 요소를 빼면 첫 번째 요소를 0으로 하는 해당 요소의 인덱스를 반환
    # 인덱스에 n을 더해 줌으로써 반환하고싶은 문자를 바꾼다.
    # 인덱스가 25인 z에서 전체 길이인 26을 나눠 줌으로써 전체를 계속 순회한다.
    # 처음에 뺏던 유니코드를 더해 줌으로써 실제 유니코드를 반환할 수 있게 한다.
    def solution(s, n):
        s = list(s)
        for i in range(len(s)):
            if s[i].isupper():
                s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
            elif s[i].islower():
                s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
        return "".join(s)