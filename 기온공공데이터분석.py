import csv
# f = open('seoul.csv', 'r', encoding='cp949')
# with open('seoul.csv', 'r', encoding='cp949') as file:
#     data = csv.reader(file, delimiter=',')
#     for row in data:
#         print(row)

with open('seoul.csv', 'r', encoding='cp949') as file:
    data = csv.reader(file)
    header = next(data)
    max_temp = -999     # 최고기온 값을 저장할 변수
    max_date = ""       # 최고기온이 가장 높았던 날짜를 저장할 변수

    for row in data:
        if row[-1] == '':
            row[-1] = -999      # 결측치 값 이였음을 표시
        row[-1] = float(row[-1])
        if max_temp < row[-1]:
            max_date = row[0]
            max_temp = row[-1]
        print(row)

print(f"기상 관측이래 서울의 최고기온이 가장 높았던 날은 {max_date}이며, {max_temp}도 였습니다.")
file.close()