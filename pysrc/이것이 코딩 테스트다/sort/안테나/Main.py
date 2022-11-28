# 아이디어 : 정확히 중간 값에 해당하는 위치에 안테나를 설치했을 때 모든 집까지의 거리의 총합이 최소가 된다.

n = int(input())

houses = sorted(list(map(int, input().split())))

print(houses[(n-1)//2])