import itertools

def solution(users, emoticons):
    dis = [10, 20, 30, 40]
    n = len(emoticons)
    dis_allcase = list(itertools.product(dis, repeat=n)) #모든 할인율 경우의 수
    result_temp = []
    for i in dis_allcase:
        emoticons_temp = emoticons.copy() 
        for j in range(0,len(emoticons_temp)): #이모티콘 가격에 할인율 적용
            emoticons_temp[j] *= (100-i[j])/100
        tmp = [] #이번 경우의 수에서 사용자들의 구매 비용을 저장
        cut_line = [] #사용자가 서비스를 가입하게되는 금액
        for k in users: 
            price = 0
            cut_line.append(k[1])
            for a in range(0, len(emoticons_temp)):
                if k[0] <= i[a]: #판매 할인율이 더 높은 경우
                    price+=emoticons_temp[a] 
            tmp.append(price) #각 사용자의 구매비용을 저장
        num = 0
        money = 0
        for b in range(0,len(tmp)):
            if tmp[b] >= cut_line[b]: #가입하게 되는 금액보다 비쌀경우 가입자 증가
                num+=1
            else: #싼 경우 이모티콘 구매
                money+=tmp[b]
        result_temp.append([num, money])
        
    answer = [0, 0]
    for x in result_temp:
        if answer[0] <= x[0]: #가입자 수를 비교
            if answer[0] < x[0]: #가입자 수가 더 많은 경우를 중시
                answer = x
            else:
                if answer[1] < x[1]: #가입자 수가 같다면 판매액 비교
                    answer = x

    return answer
