def solution(today, terms, privacies):
    answer = []
    year_temp = int(today[:4])
    month_temp = int(today[5:7])
    day_temp = int(today[8:10])
    terms_alpha = []
    terms_num = []
    for x in range(0, len(terms)):
        terms_alpha.append(terms[x][0])
        terms_num.append(int(terms[x][2:]))
        
    for i in range(0, len(privacies)):
        terms_temp = terms_num[terms_alpha.index(privacies[i][-1])]
        pri_year_temp = int(privacies[i][0:4]) #수집한 년도
        pri_month_temp = int(privacies[i][5:7]) #수집한 달
        pri_day_temp = int(privacies[i][8:10]) #수집한 일자
        
        pri_month_temp+=terms_temp
        if pri_day_temp != 1:  #수집일자가 1일이 아니면 단순 n달 후 -1일
            pri_day_temp-=1
            while pri_month_temp > 12:
                pri_year_temp+=1
                pri_month_temp-=12
        elif pri_day_temp == 1:  #수집일자가 1일이면 n-1달 후 28일
            pri_day_temp = 28
            pri_month_temp-=1
            while pri_month_temp > 12:
                pri_year_temp+=1
                pri_month_temp-=12
        
        if (year_temp == pri_year_temp): #같은 년도면
            if (month_temp == pri_month_temp): #같은 달이면
                if (pri_day_temp < day_temp ): #유효일을 넘긴 경우
                    answer.append(i+1)
            elif (pri_month_temp < month_temp): #유효달을 지난 경우
                answer.append(i+1)
        elif (year_temp > pri_year_temp): #유효년을 지난 경우
            answer.append(i+1)
    return answer
