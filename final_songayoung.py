import pandas as pd
import matplotlib.pyplot as plt
import platform
from matplotlib import rc
from matplotlib import font_manager

plt.rcParams['font.size'] = 17


if platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name() #원하는 폰트 ttf
    rc('font', family=font_name)
elif platform.system() == 'Darwin': # Mac
    rc('font', family='AppleGothic')
else: #linux
    rc('font', family='NanumGothic')

df= pd.read_csv("경찰청_범죄 발생 지역별 통계_20151231.csv", encoding='cp949')

crime_types = df['범죄중분류'].unique() 
regions = ['서울', '부산', '대구', '인천', '광주', '대전', '울산','세종']  # 분석할 지역

# 범죄 유형과 지역별 범죄 발생 건수
crime_data = {}
for crime_type in crime_types:
    crime_data[crime_type] = []
    for region in regions:
        count = df.loc[df['범죄중분류'] == crime_type, region].values[0]
        crime_data[crime_type].append(count)

# 데이터 시각화
plt.figure(figsize=(12, 8))
for crime_type in crime_data:
    plt.plot(regions, crime_data[crime_type], marker='o', label=crime_type)

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.title('지역별 범죄 발생 건수')
plt.xlabel('지역')
plt.ylabel('범죄 발생 건수')
plt.legend(loc='right')
plt.grid(True)
plt.show()

# 지역별 범죄 발생 현황 시각화
df_grouped = df.groupby('범죄중분류').sum()
df_grouped.loc[:, '서울':'세종'].plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('지역별 범죄 발생 현황')
plt.xlabel('범죄 유형')
plt.ylabel('범죄 발생 건수')
plt.legend(title='지역', bbox_to_anchor=(1.05, 1))
plt.show()

# 교통범죄
traffic_crimes = df[df['범죄중분류'] == '교통범죄']

region_counts = traffic_crimes.loc[:, '서울':'세종'].sum()

top_regions = region_counts.nlargest(4)

top_regions.plot(kind='bar', figsize=(8, 6))
plt.title('교통범죄 발생 건수 상위 4개 지역')
plt.xlabel('지역')
plt.ylabel('범죄 발생 건수')
plt.ylim(0, 100000)
plt.show()

# 사기
fraudulent_crimes = df[df['범죄중분류'] == '사기']

region_counts = fraudulent_crimes.loc[:, '서울':'세종'].sum()

top_regions = region_counts.nlargest(4)

top_regions.plot(kind='bar', figsize=(8, 6))
plt.title('사기 발생 건수 상위 4개 지역')
plt.xlabel('지역')
plt.ylabel('범죄 발생 건수')
plt.ylim(0, 100000)
plt.show()

# 절도
theft_crimes = df[df['범죄중분류'] == '절도']

region_counts = theft_crimes.loc[:, '서울':'세종'].sum()

top_regions = region_counts.nlargest(4)

top_regions.plot(kind='bar', figsize=(8, 6))
plt.title('절도 발생 건수 상위 4개 지역')
plt.xlabel('지역')
plt.ylabel('범죄 발생 건수')
plt.ylim(0, 100000)
plt.show()