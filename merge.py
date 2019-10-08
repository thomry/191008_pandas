import pandas as pd

person  = pd.read_csv('survey_person.csv')
site    = pd.read_csv('survey_site.csv')
survey  = pd.read_csv('survey_survey.csv')
visited = pd.read_csv('survey_visited.csv')

# visited dataframe의 일부만 사용할 것
visited_subset = visited.loc[[0, 2, 6], ]
# merge 메서드는 기본적으로 내부 조인. lef_on(왼쪽)을 site로 지정. right_on을 visited_subset으로 지정.
# left_on과 right_on의 열의 값이 일치하면 왼쪽을 기준으로 연결함.
o2o_merge = site.merge(visited_subset, left_on = 'name', right_on = 'site')
print(o2o_merge)
# name이랑 site를 맞추어 left_on의 'name'열과 'site에 맞추어 site data가 복사됨
o2o_merge = site.merge(visited, left_on = 'name', right_on = 'site')
print(o2o_merge)
print('-'*100)

ps = person.merge(survey, left_on='ident', right_on='person')
vs = visited.merge(survey, left_on='ident', right_on='taken')
print(ps)
print(vs)
# lef_on, right_on에 전달한느 값은 여러개라도 상관이 없습니다.
# _x는 왼쪽 dataframe 열을 의미 _y는 오른쪽 dataframe 열 의미
ps_vs = ps.merge(vs, left_on=['ident', 'taken', 'quant', 'reading'], right_on=['person', 'ident', 'quant', 'reading'])
print(ps_vs)
