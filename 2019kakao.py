#2019 카카오 겨울 인턴십 징검다리 건너기 문제 풀이

def calc(stones, k, mid):
    now = 0
    for stone in stones:
        if (stone < mid): 
            now += 1
        else:
            now = 0
        if(now >= k):
            return False
    return True

def solution(stones, k):
    if k==1: 
        return min(stones)
    
    start = 1
    end = max(stones)

    while(start < end - 1):
        mid = (start + end) // 2
        if (calc(stones, k, mid)):
            start = mid
        else:
            end = mid
    return start