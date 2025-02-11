import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import matplotlib

#------------------------------- 한국어 활성화
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
#-------------------------------


#-------------------------------  데이터 추출
url = 'https://ko.wikipedia.org/wiki/2019%EB%85%84_%EA%B0%80%EC%98%A8_%EB%94%94%EC%A7%80%ED%84%B8_%EC%B0%A8%ED%8A%B8_1%EC%9C%84_%EB%AA%A9%EB%A1%9D'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', {'class': 'wikitable'})
df = pd.read_html(str(table))[0]
#-------------------------------

#------------------그래프 구현
df_avg = df.groupby('노래')['가온 지수'].mean().reset_index()

song= df_avg['노래']
P = df_avg['가온 지수']
colors = ['red', 'blue', 'green', 'purple']

plt.bar(song, P, color = colors)


plt.title("2019년 가을 차트 순위 - 노래별 듣는 사람 수")
plt.xlabel("노래")
plt.ylabel("가온 지수")


plt.xticks(rotation=90)


plt.show()
#-------------------

