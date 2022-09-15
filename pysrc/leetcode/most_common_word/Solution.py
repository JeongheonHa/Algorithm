from typing import List
import collections, re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 금지 문자열을 제외한 모든 문자를 소문자 문자열 리스트로 만든다.
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        # words리스트를 Counter 객체로 변환
        counts = collections.Counter(words)
        # 가장 많이 등장하는 단어를 포함한 요소의 [0][0]값을 출력
        return counts.most_common(1)[0][0]