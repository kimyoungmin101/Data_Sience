x = list(input().split())
Q = x[20:]
for i in Q:
  if(i == 'IFRS연결' or i in 'E'):
    Q.remove(i)

title = Q[:6] # 연도
title[5] = '2020.12' 
Q = Q[8:]

earning = Q[:6] # 매출액
Q = Q[7:]

benefit = Q[:6] # 영업이익
Q = Q[7:]

besoon = Q[:6] # 순이익

'''
print(Q)
print('연도', title)
print('매출액', earning)
print('영업이익', benefit) 
print('순이익', besoon)
'''
result = []
for i in range(6):
  result.append([title[i], earning[i], benefit[i], besoon[i]])
# 연도, 매출액, 영업이익, 순이익

del result[1]
A = result[3]
del result[3]
result.insert(0, A)

for i in range(len(result)):
  result[i] = result[i][1:]

arr = []
for i in result:
  for j in i:
    j = str(j)
    j = j.replace(",", "")
    arr.append(int(j))
  
for i in arr:
  print(i, end="  ")
