#입력받는 데이터 별로 분류된 리스트트
student_num = []
name = []
en = []
c = []
py = []
total = []

#메뉴 함수
def menu():
    print("========성적관리 프로그램========")
    print("1. 학생 정보 입력")
    print("2. 성적 조회")
    print("3. 성적 수정")
    print("4. 성적 삭제")
    print("5. 종료")
    print("=================================")
    print("메뉴를 선택하세요 : ", end="")
    return int(input())

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
    total.sort(reverse=True)
    current_rank = total.index(total[number]) + 1
    return current_rank

#출력함수
def prin(n):
    print(student_num[n],'\t',name[n],'\t',en[n],'\t',c[n],'\t',py[n],'\t',total[n],'\t',grade_score(total[n]/3),'\t',rank(n))

#메인 프로그램
while True:
    m = menu()
    if m == 1: #학생정보입력
        print("\n=== 학생 정보 입력 ===")
        for i in range(5):
            print(i+1,"번째 학생 정보 입력")
            get_score()
        sum_f()
    elif m == 2: #성적조회
        if len(student_num) == 0:
            print("등록된 학생이 없습니다.")
            continue
        print("\n성적관리 프로그램")
        print("===============================================================================")
        print("학번",'\t',"이름",'\t',"영어",'\t',"C-언어",' ',"파이썬",' ',"총점",' ',"학점",' ',"등수")
        print("===============================================================================")
        for i in range(len(student_num)):
            prin(i)
        print("===============================================================================")
    elif m == 3: #성적수정
        if len(student_num) == 0:
            print("등록된 학생이 없습니다.")
            continue
        print("수정하실 학번을 입력하세요.")
        num = int(input())
        n = student_num.index(num)
        print("수정할 학생의 이름을 입력하세요.")
        name[n] = str(input())
        print("수정할 영어 점수를 입력하세요.")
        en[n] = int(input())
        print("수정할 C-언어 점수를 입력하세요.")
        c[n] = int(input())
        print("수정할 파이썬 점수를 입력하세요.")
        py[n] = int(input())
        sum_f()
        print("수정이 완료되었습니다.")
    elif m == 4: #성적삭제
        if len(student_num) == 0:
            print("등록된 학생이 없습니다.")
            continue
        print("삭제하실 학번을 입력하세요 :", end="")
        num = int(input())
        n = student_num.index(num)
        student_num.pop(n)
        name.pop(n)
        en.pop(n)
        c.pop(n)
        py.pop(n)
        total.pop(n)
        print("삭제가 완료되었습니다.")
    elif m == 5: #종료
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 메뉴 선택입니다.")