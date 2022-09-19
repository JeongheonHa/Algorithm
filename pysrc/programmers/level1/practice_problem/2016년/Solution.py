class Solution:
    def solution(a, b):
    # % 7의 나머지가 1이 나오면 인덱스 1이 금요일이게 설정
        week = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
        month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        return week[(sum([day for day in month[:a-1]]) + b) % 7]