def solution(s):
    answer = 0
    alphaNum = ["zero", "one", "two", "three", "four", "five", 
                "six", "seven", "eight", "nine"]
    
    for idx, num in enumerate(alphaNum):
        if num in s:
            s = s.replace(num, str(idx))
    
    answer = int(s)
    return answer