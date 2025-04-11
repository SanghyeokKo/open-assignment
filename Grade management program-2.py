  #######################################################################################################################

  #프로그램명: 2주차 성적관리 프로그램

  #작성자: 소프트웨어학부/고상혁

  #작성일: 2025-03-12

  #프로그램 설명: 5명의 학생의 세개의 교과목 (영어, C-언어, 파이썬)에 대하여  키보드로부터 입력받아 총점, 평균, 학점, 등수를 계산하는 프로그램 작성

  #######################################################################################################################
en = []
c = []
py = []
sum_en = 0
sum_c = 0
sum_py = 0
print("학생1부터 학생5까지 영어 점수를 입력하세요")
for i in range(5):
    en.append(int(input()))
    sum_en += en[i]
print("학생1부터 학생5까지 c언어 점수를 입력하세요")
for i in range(5):
    c.append(int(input()))
    sum_c += c[i]
print("학생1부터 학생5까지 파이썬 점수를 입력하세요")
for i in range(5):
    py.append(int(input()))
    sum_py += py[i]
print("\n")
print("영어 총점은",sum_en,"점 입니다")
print("c언어 총점은",sum_c,"점 입니다")
print("파이썬 총점은",sum_py,"점 입니다")
print("\n")
print("영어 평균은",sum_en/5,"점 입니다")
print("c언어 평균은",sum_c/5,"점 입니다")
print("파이썬 평균은",sum_py/5,"점 입니다")
print("\n")
for i in range(5):
    if en[i] >= 90:
        print(i+1,"번 학생의 영어학점은 A입니다")
    elif en[i] >= 80:
        print(i+1,"번 학생의 영어학점은 B입니다")
    elif en[i] >= 70:
        print(i+1,"번 학생의 영어학점은 C입니다")
    elif en[i] >= 60:
        print(i+1,"번 학생의 영어학점은 D입니다")
    else:
        print(i+1,"번 학생의 영어학점은 F입니다")
for i in range(5):
    if c[i] >= 90:
        print(i+1,"번 학생의 c언어학점은 A입니다")
    elif c[i] >= 80:
        print(i+1,"번 학생의 c언어학점은 B입니다")
    elif c[i] >= 70:
        print(i+1,"번 학생의 c언어학점은 C입니다")
    elif c[i] >= 60:
        print(i+1,"번 학생의 c언어학점은 D입니다")
    else:
        print(i+1,"번 학생의 c언어학점은 F입니다")
for i in range(5):
    if py[i] >= 90:
        print(i+1,"번 학생의 파이썬학점은 A입니다")
    elif py[i] >= 80:
        print(i+1,"번 학생의 파이썬학점은 B입니다")
    elif py[i] >= 70:
        print(i+1,"번 학생의 파이썬학점은 C입니다")
    elif py[i] >= 60:
        print(i+1,"번 학생의 파이썬학점은 D입니다")
    else:
        print(i+1,"번 학생의 파이썬학점은 F입니다")
print("\n")
for i in range(5):
    max_en = max(en)
    for j in range(5):
        if en[j] == max_en and max_en != 0:
            print("영어",i+1,"등은",j+1,"번 학생입니다")
            en[j] = 0
for i in range(5):
    max_c = max(c)
    for j in range(5):
        if c[j] == max_c and max_c != 0:
            print("c언어",i+1,"등은",j+1,"번 학생입니다")
            c[j] = 0
for i in range(5):
    max_py = max(py)
    for j in range(5):
        if py[j] == max_py and max_py != 0:
            print("파이썬",i+1,"등은",j+1,"번 학생입니다")
            py[j] = 0