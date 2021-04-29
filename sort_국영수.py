# 국어 점수는 감소
# 국어 점수가 같다면 영어 점수는 증가
# 국영 점수가 같다면 수학 점수는 감소
# 모든 점수가 같다면 이름이 사전순으로 증가하는 순서(대 -> 소)

n = int(input('Number of students:',))
students = [input('Name, kor, eng, math').split() for _ in range(n)]
name, kor, eng, math = 0, 1, 2, 3

students.sort(key=lambda x: (-int(x[kor]), int(x[eng]), -int(x[math]), x[name]))

for stu in students:
    print(stu[name])
