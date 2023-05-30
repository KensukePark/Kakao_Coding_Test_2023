import math

def dfs(x, parent_node):
    # 노드가 0인 경우 자식노드는 전부 0이여야함
    if parent_node == '0' and not all(child_node == '0' for child_node in x):
        return False
    if len(x) == 1:
        return True
    mid = len(x) // 2
    return dfs(x[:mid], x[mid]) and dfs(x[mid+1:], x[mid])
    
def solution(numbers):
    answer = []
    bin_list = []
    for i in numbers:
        temp = bin(i)[2:]
        log_temp = 2 ** (int(math.log(len(temp), 2)) + 1) - 1 #n단 인 경우 2**n-1이여야함
        num = ('0' * (log_temp - len(temp)) + temp) #포화이진트리가 되게 맞춰줌
        if dfs(num, num[len(num) // 2]):
            answer.append(1)
        else: answer.append(0)
    return answer
