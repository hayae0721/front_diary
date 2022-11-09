"""
[그림일기(그림)에서 인식된 그림 개수 daily 통계 & 시각화]
- 그림일기에서 그린(인식된) 그림(객체) 막대그래프 통계 도출
"""
import matplotlib.pyplot as plt
import platform
import numpy as np

from datetime import datetime

time = datetime.today().strftime("%Y-%m-%d")
user_name = 'user_name'

# matplotlib 패키지 한글 깨짐 처리 시작
if platform.system() == 'Darwin':     # mac os
        plt.rc('font', family='AppleGothic')
elif platform.system() == 'Windows':  # 윈도우
        plt.rc('font', family='Malgun Gothic')
elif platform.system() == 'Linux':    # 리눅스 (구글 콜랩)
        #!wget "https://www.wfonts.com/download/data/2016/06/13/malgun-gothic/malgun.ttf"
        #!mv malgun.ttf /usr/share/fonts/truetype/
        #import matplotlib.font_manager as fm
        #fm._rebuild()
        plt.rc('font', family='Malgun Gothic')


# 추후에 인식된 list를 받아오는걸로 변경
years = ['집', '사람', '꽃', '나무', '개구리', '공룡', '강아지']
x = np.arange(len(years))
values = [1, 2, 10, 4, 2, 1, 1]

plt.bar(x, values, align='edge', edgecolor='lightgray',
        linewidth=5, tick_label=years)
plt.xlabel(f"{time} {user_name} 그림 종류 분류")
plt.ylabel("각 그림별 빈도 수")

plt.show()