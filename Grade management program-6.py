  #######################################################################################################################

  #프로그램명: 5주차 성적관리 프로그램

  #작성자: 소프트웨어학부/고상혁

  #작성일: 2025-04-11

  #프로그램 설명: 5명의 학생의 세개의 교과목 (영어, C-언어, 파이썬)에 대하여 
  #             키보드로부터 학번, 이름, 영어점수, C-언어 점수, 파이썬 점수를 입력받아 총점, 평균, 학점, 등수를  계산하는 프로그램 작성
  #             -입력 함수, 총점/평균 계산 함수,  학점계산 함수, 등수계산 함수, 출력 함수 
  #             - 삽입 함수, 삭제 함수, 탐색함수(학번, 이름), 정렬(총점)함수, 80점이상 학생 수 카운트 함수 

  #######################################################################################################################

# Student 클래스 정의
class Student:
    def __init__(self, student_num, name, en, c, py):
        self.student_num = student_num
        self.name = name
        self.en = en
        self.c = c
        self.py = py
        self.total = en + c + py    #총점 계산
        self.grade = self.calculate_grade() #학점 계산
    
    def calculate_grade(self): #학점 계산
        avg = self.total / 3
        if avg >= 95:
            return "A+"
        elif avg >= 90:
            return "A"
        elif avg >= 85:
            return "B+"
        elif avg >= 80:
            return "B"
        elif avg >= 75:
            return "C+"
        elif avg >= 70:
            return "C"
        elif avg >= 65:
            return "D+"
        elif avg >= 60:
            return "D"
        elif avg >= 50:
            return "E"
        else:
            return "F"
    
    def update_scores(self, en, c, py):
        self.en = en
        self.c = c
        self.py = py
        self.total = en + c + py
        self.grade = self.calculate_grade()

# 학생 리스트
students = []

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
def get_score():
    print("학번 : ", end="")
    student_num = int(input())
    print("이름 : ", end="")
    name = str(input())
    print("영어 : ", end="")
    en = int(input())
    print("C-언어 : ", end="")
    c = int(input())
    print("파이썬 : ", end="")
    py = int(input())
    return Student(student_num, name, en, c, py)

#등수계산 함수
def calculate_rank(student):
    sorted_students = sorted(students, key=lambda x: x.total, reverse=True)
    return sorted_students.index(student) + 1

#출력함수
def print_student(student):
    rank = calculate_rank(student)
    print(f"{student.student_num}\t{student.name}\t{student.en}\t{student.c}\t{student.py}\t{student.total}\t{student.grade}\t{rank}")

#메인 프로그램
while True:
    m = menu()
    if m == 1: #학생정보입력
        print("\n=== 학생 정보 입력 ===")
        for i in range(5):
            print(f"{i+1}번째 학생 정보 입력")
            students.append(get_score())
    elif m == 2: #성적조회
        if len(students) == 0:
            print("등록된 학생이 없습니다.")
            continue
        print("\n성적관리 프로그램")
        print("===============================================================================")
        print("학번",'\t',"이름",'\t',"영어",'\t',"C-언어",' ',"파이썬",' ',"총점",' ',"학점",' ',"등수")
        print("===============================================================================")
        for student in students:
            print_student(student)
        print("===============================================================================")
    elif m == 3: #성적수정
        if len(students) == 0:
            print("등록된 학생이 없습니다.")
            continue
        print("수정하실 학번을 입력하세요.")
        num = int(input())
        student = next((s for s in students if s.student_num == num), None)
        if student:
            print("수정할 학생의 이름을 입력하세요.")
            name = str(input())
            print("수정할 영어 점수를 입력하세요.")
            en = int(input())
            print("수정할 C-언어 점수를 입력하세요.")
            c = int(input())
            print("수정할 파이썬 점수를 입력하세요.")
            py = int(input())
            student.name = name
            student.update_scores(en, c, py)
            print("수정이 완료되었습니다.")
        else:
            print("해당 학번의 학생이 없습니다.")
    elif m == 4: #성적삭제
        if len(students) == 0:
            print("등록된 학생이 없습니다.")
            continue
        print("삭제하실 학번을 입력하세요 :", end="")
        num = int(input())
        student = next((s for s in students if s.student_num == num), None)
        if student:
            students.remove(student)
            print("삭제가 완료되었습니다.")
        else:
            print("해당 학번의 학생이 없습니다.")
    elif m == 5: #종료
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 메뉴 선택입니다.")