#3주차 성적 관리 프로그램
#입력받는 데이터 별로 분류된 리스트트
student_num = []
name = []
en = []
c = []
py = []
total = []

#입력 함수
def get_score ():
    print("학번 : ", end="")
    student_num.append(int(input()))
    print("이름 : ", end="")
    name.append(str(input()))
    print("영어 : ", end="")
    en.append(int(input()))
    print("C-언어 : ", end="")
    c.append(int(input()))
    print("파이썬 : ", end="")
    py.append(int(input()))

#총점 계산 함수
def sum_f():
    total.clear()
    for i in range(5):  
        total.append(en[i] + c[i] + py[i])

#학점 계산 함수
def grade_score (score):
    if score >= 95:
        return "A+"
    elif score >= 90:
        return "A"
    elif score >= 85:
        return "B+"
    elif score >= 80:
        return "B"
    elif score >= 75:
        return "C+"
    elif score >= 70:
        return "C"
    elif score >= 65:
        return "D+"
    elif score >= 60:
        return "D"
    elif score >= 50:
        return "E"
    else:
        return "F"

#등수계산 함수
def rank(number):
    current_rank = 1
    for i in range(5):
        if total[number] < total[i]:
            current_rank += 1
    return current_rank

#출력함수
def prin(n):
    print(student_num[n],'\t',name[n],'\t',en[n],'\t',c[n],'\t',py[n],'\t',total[n],'\t',grade_score(total[n]/3),'\t',rank(n))
#학생 정보 입력력
for i in range(5):
    get_score()
#총점 계산
sum_f()
#출력
print("성적관리 프로그램")
print("===============================================================================")
print("학번",'\t',"이름",'\t',"영어",'\t',"C-언어",'\t',"파이썬",'\t',"총점",'\t',"학점",'\t',"등수")
print("===============================================================================")
for i in range(5):
    prin(i)
