from numpy import NAN, NaN, nan
import pandas as pd

# 누락값은 말 그대로 데이터가 없다는 뜻이므로 BOOLEAN이나 빈공백열, 0과 FALSE값을 낳는다. 다만 PANDAS로 확인이 가능
# 반대로 누락값이 아닌 경우를 검사할 때에는 .notnull()사용하면 됩니다.
print(pd.isnull(NaN))
print(pd.isnull(nan))
print(pd.isnull(NAN))

survey  = pd.read_csv('survey_survey.csv')
visited = pd.read_csv('survey_visited.csv')


