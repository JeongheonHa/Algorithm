from typing import List
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 기본값이 []인 defaultdict객체 생성
        anagrams = collections.defaultdict(list)    # 존재하지 않는 키를 넣을 경우 KeyError 발생하므로 defaultdict으로 생성
        
        for word in strs:
            # key에 따라 word(value)추가
            anagrams[''.join(sorted(word))].append(word)    # 애너그램 관계에 있는 단어를 정렬함으로써 동일한 단어로 만든다.
        # value 값만 리스트로 반환
        return list(anagrams.values())