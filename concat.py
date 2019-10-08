import pandas as pd

df1 = pd.read_csv('concat_1.csv')
df2 = pd.read_csv('concat_2.csv')
df3 = pd.read_csv('concat_3.csv')

row_concat = pd.concat([df1,df2,df3])

# 열이름 유지. 데이터를 연결하여 전달됨. 이름도 유지.
print(row_concat)
print('-'*100)

# dataframe에서 네번째행 추출해보기
print(row_concat.iloc[3, ])
print('-'*100)

# dataframe에 series추가해보기
# 리스트를 시리즈로 변환
new_row_series = pd.Series(['n1','n2','n3','n4'])
print(pd.concat([df1,new_row_series]))
print('-'*100)
# new_row_series는 새로운 열로 추가가되며 누락값(NaN)이 생김

# 행1개의 dataframe을 생성하여 연결
new_row_df = pd.DataFrame([['n1','n2','n3','n4']], columns=['A','B','C','D'])
print(new_row_df)
print('-'*100)

# 연결할 dataframe이 1개일 경우 append사용가능
# ignore_index=True는 연결 후 dataframe index를 0부터 다시 지정함.
print(df1.append(new_row_df))
data_dict={'A':'n1', 'B':'n2', 'C':'n3', 'D':'n4'}
print(df1.append(data_dict, ignore_index=True))
print('-'*100)

# 열 방향으로 데이터 연결. axis = 1입력시 열로 연결, axis 평소 기본값은 0입니다.
# 연결 후, 열이름으로 데이터 추출하기. 새로운 열 추가.
# ignore_index 열방향 데이터연결에서 사용. 열의 번호가 순서대로 매겨집니다.
col_concat = pd.concat([df1, df2, df3], axis = 1)
print(col_concat)
print(col_concat['A'])
col_concat['new_col_list']=['n1','n2','n3','n4']
print(col_concat)
print(pd.concat([df1, df2, df3], axis=1, ignore_index=True))
print('-'*100)

# 공통 열과 공통 index만 연결해보기. 기존 데이터 열이름 새롭게 부여.
df1.columns = ['A','B','C','D']
df2.columns = ['E','F','G','H']
df3.columns = ['A','C','F','H']
# 그대로 출력 시, 누락값 발생
# 사전 순으로 조인 키로 dataframe 정렬함. true는 기본값, false는 많을 때 성능향상
row_concat = pd.concat([df1, df2, df3], sort=True)
print(row_concat)
# 누락값을 없애려는 방법은 join = 'inner'
print(pd.concat([df1, df2, df3], join='inner'))
# 그러나 df1, df2, df3의 공통 열이 없어 empty dataframe이 결과값으로 출력됨
# df1과 df3의 공통열만 골라 연결해보기
print(pd.concat([df1, df3],ignore_index=False, join='inner'))
print('-'*100)

# dataframe 행방향으로 연결해보기
# df1, df2, df3의 index를 다시 지정
df1.index = [0, 1, 2, 3]
df2.index = [4, 5, 6, 7]
df3.index = [0, 2, 5, 7]
col_concat = pd.concat([df1, df2, df3], axis=1)
print(col_concat)
# df1, df3의 공통열만 골라 연결해보기
print(pd.concat([df1, df3], axis=1, join='inner'))