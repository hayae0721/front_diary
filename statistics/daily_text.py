import matplotlib.pyplot as plt
import platform

from datetime import datetime

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

plt.rcParams['axes.unicode_minus'] = False  # 한글 폰트 사용시 마이너스 폰트 깨짐 해결
# matplotlib 패키지 한글 깨짐 처리 끝

# 통계 시작
def statistics_pie_char(time: datetime.today(), user_name: str):
        # pie chart를 사용할 때, 원의 형태를 유지하기 위한 명령어
        plt.axis('equal')

        # 추후에 text 감정분석 파트가 개발 완료가 되면 검출된 감정들을 list로 받고 (중요: 중복 허용해야함)
        # sizes는 각 감정의 개수만큼으로 비율화
        # 위 두 사항을 적용해서 static이 아닌 변화형 pie chart 출력하도록 수정
        labels = ['우울', '두려움', '행복', '중립']
        sizes = [15, 30, 45, 10]
        colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
        explode = (0, 0.1, 0, 0)
        plt.title(f"{time} {user_name} 심리분석 결과")
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')

        # 그래프 출력
        # plt.show()
        # 그래프 저장
        plt.savefig(f'/Users/sharekim_hangyuseong/Desktop/{time} {user_name}.jpg')


if __name__ == '__main__':
        time = datetime.today().strftime("%Y-%m-%d")

        statistics_pie_char(time, user_name='user_name')