 #######################################################################################################################

 #프로그램명: 2주차 성적관리 프로그램

 #작성자: 소프트웨어학부/고상혁

 #작성일: 2025-03-12

 #프로그램 설명: 5명의 학생의 세개의 교과목 (영어, C-언어, 파이썬)에 대하여 

 #        키보드로부터 학번, 이름, 영어점수, C-언어 점수, 파이썬 점수를 입력받아 총점, 평균, 학점, 등수를 계산하는 프로그램 작성

 #       - 입력 함수, 총점/평균 계산 함수,  학점계산 함수, 등수계산 함수, 출력 함수로 나누어 구현

 #       - 입력 형식

 #          학번:

 #         이름:

 #           영어

 #            C-언어:

 #            파이썬:

 #       - 출력 형식
 #                                        성적관리 프로그램         

 #         =============================================================================

 #           학번        이름    영어    C-언어    파이썬    총점   평균   학점      등수      

 #         ==============================================================================

 #         2025041001   홍길동   80     88        90      256    86     B+       1  

 #######################################################################################################################
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
