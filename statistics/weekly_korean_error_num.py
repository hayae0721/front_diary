import matplotlib.pyplot as plt
import platform

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
def statistics_korean_error_num_char(user_name: str, error_list: list):
    plt.plot(
                ['월', '화', '수', '목', '금', '토', '일'],  # x point (1~7일)
                error_list,                   # y point (해당 날에 검출된 맞춤법 에러 수)
                c="b", lw=5, ls="--", marker="o", ms=15, mec="g", mew=5, mfc="r"
    )
    plt.title(f"weekly {user_name} 맞춤법 오류 수 통계")

    # 그래프 시각화
    # plt.show()
    # 그래프 저장
    plt.savefig(f'/Users/sharekim_hangyuseong/Desktop/{user_name}.jpg')

if __name__ == '__main__':
    # 추후에 월화수목금토일 요일별 맞춤별 오류 수를 담은 List를 가져오도록 수정할 것.
    statistics_korean_error_num_char(user_name='user_name', error_list=[9, 7, 8, 5, 8, 4, 2])