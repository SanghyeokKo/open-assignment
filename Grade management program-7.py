  #######################################################################################################################

  #프로그램명: 11주차 성적관리 프로그램

  #작성자: 소프트웨어학부/고상혁

  #작성일: 2025-05-24

  #프로그램 설명: 5명의 학생의 세개의 교과목 (영어, C-언어, 파이썬)에 대하여 
  #             키보드로부터 학번, 이름, 영어점수, C-언어 점수, 파이썬 점수를 입력받아 총점, 평균, 학점, 등수를  계산하는 프로그램 작성
  #             -입력 함수, 총점/평균 계산 함수,  학점계산 함수, 등수계산 함수, 출력 함수 
  #             - 삽입 함수, 삭제 함수, 탐색함수(학번, 이름), 정렬(총점)함수, 80점이상 학생 수 카운트 함수 
  #             - 데이터베이스 연결, 학생 정보 저장, 조회, 수정, 삭제 기능 추가
  #######################################################################################################################
import mysql.connector

# DB 연결 설정
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="m458rhtkdgur:",
    database="grade_management"
)
cursor = conn.cursor()

# 학점 계산 함수
def calculate_grade(avg):
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

# 입력 함수
def insert_student():
    student_num = int(input("학번: "))
    name = input("이름: ")
    en = int(input("영어: "))
    c = int(input("C-언어: "))
    py = int(input("파이썬: "))
    total = en + c + py
    avg = total / 3
    grade = calculate_grade(avg)

    query = "INSERT INTO student_list VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (student_num, name, en, c, py, total, grade)
    cursor.execute(query, values)
    conn.commit()
    print("학생 정보가 저장되었습니다.")

# 조회 함수
def display_students():
    cursor.execute("SELECT * FROM student_list ORDER BY total DESC")
    rows = cursor.fetchall()

    if not rows:
        print("등록된 학생이 없습니다.")
        return

    print("학번\t\t이름\t영어\tC\t파이썬\t총점\t학점\t등수")
    for idx, row in enumerate(rows):
        print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}\t{idx+1}")

# 수정 함수
def update_student():
    student_num = int(input("수정할 학번 입력: "))
    cursor.execute("SELECT * FROM student_list WHERE student_num=%s", (student_num,))
    if not cursor.fetchone():
        print("해당 학번이 존재하지 않습니다.")
        return

    name = input("이름: ")
    en = int(input("영어: "))
    c = int(input("C-언어: "))
    py = int(input("파이썬: "))
    total = en + c + py
    avg = total / 3
    grade = calculate_grade(avg)

    query = """UPDATE student_list
               SET name=%s, en=%s, c=%s, py=%s, total=%s, grade=%s 
               WHERE student_num=%s"""
    values = (name, en, c, py, total, grade, student_num)
    cursor.execute(query, values)
    conn.commit()
    print("수정 완료.")

# 삭제 함수
def delete_student():
    student_num = int(input("삭제할 학번 입력: "))
    cursor.execute("DELETE FROM student_list WHERE student_num=%s", (student_num,))
    conn.commit()
    print("삭제 완료.")

# 메뉴
def menu():
    print("\n===== 성적 관리 프로그램 =====")
    print("1. 학생 정보 입력")
    print("2. 성적 조회")
    print("3. 성적 수정")
    print("4. 성적 삭제")
    print("5. 종료")
    return int(input("메뉴 선택: "))

# 메인 루프
while True:
    m = menu()
    if m == 1:
        insert_student()
    elif m == 2:
        display_students()
    elif m == 3:
        update_student()
    elif m == 4:
        delete_student()
    elif m == 5:
        print("프로그램 종료.")
        break
    else:
        print("잘못된 메뉴입니다.")
