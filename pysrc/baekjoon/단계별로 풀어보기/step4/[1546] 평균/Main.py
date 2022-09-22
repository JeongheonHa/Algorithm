n = int(input())

scores = list(map(float, input().split()))
new_scores = []

for score in scores:
    new_scores.append(score*100 / (max(scores)))
    
print(sum(new_scores)/n)