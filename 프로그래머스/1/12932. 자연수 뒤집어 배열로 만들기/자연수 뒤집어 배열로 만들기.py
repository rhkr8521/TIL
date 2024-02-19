def solution(n):
    answer = []
    
    temp = []
    strr = str(n)
    
    for i in strr:
        temp.append(i)
    
    for i in temp:
        answer.append(int(i))
    answer.reverse()
    return answer