from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        # 리스트의 요소인 문자열을 하나하나 꺼낸다.
        for log in logs:
            # 식별자를 제외한 리스트의 log들이 숫자인지 문자인지 판단
            if log.split()[1].isdigits():
                digits.append(log)
            else:
                letters.append(log)
        # 동일한 문자는 식별자 순으로 정렬
        letters.sort(key = lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits