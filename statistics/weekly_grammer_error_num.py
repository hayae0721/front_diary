"""
[그림일기(텍스트)에서 맞춤법 틀린 개수 weekly 통계 & 시각화]
- 일기(텍스트)에서 형태소와 맞춤법 틀린 수로 통계 도출
- python (서버)단에서 현재 요일이 월요일이면 부모님(선생님)한테 해당 이미지 dm 보내도록 자동화 설정 필요
"""
import matplotlib.pyplot as plt
import platform
import numpy as np

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


def statistics_korean_error_num_char(user_name: str, morpheme_num: list, grammer_error: list):
    # 2. 데이터 준비
    x = np.array(['월', '화', '수', '목', '금', '토', '일'])
    y1 = np.array([1, 3, 7, 5, 9, 7, 14])   # grammer_error
    y2 = np.array([1, 3, 5, 7, 9, 11, 13])  # morpheme_num

    # 3. 그래프 그리기
    fig, ax1 = plt.subplots()

    ax1.plot(x, y1, '-s', color='green', markersize=7, linewidth=5, alpha=0.7, label='맞춤법 에러 수')
    ax1.set_ylim(0, 18)
    ax1.set_xlabel('weekly ' + user_name + ' 맞춤법 오류 수 통계')
    ax1.tick_params(axis='both', direction='in')

    ax2 = ax1.twinx()
    ax2.bar(x, y2, color='deeppink', label='문장 내 형태소 사용 수', alpha=0.7, width=0.7)
    ax2.set_ylim(0, 18)
    # ax2.set_ylabel(r'Demand ($\times10^6$)')
    ax2.tick_params(axis='y', direction='in')

    ax1.set_zorder(ax2.get_zorder() + 10)
    ax1.patch.set_visible(False)

    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    # 그래프 출력
    plt.show()
    # 그래프 저장
    # plt.savefig(f'/Users/sharekim_hangyuseong/Desktop/{user_name}.jpg')

if __name__ == '__main__':
    # 추후에 월화수목금토일 {user_name} {요일별 문장 내 형태소 수} {요일별 맞춤별 오류 수} 를 담은 List를 가져오도록 수정할 것.
    statistics_korean_error_num_char(user_name='user_name', morpheme_num=[], grammer_error=[9, 7, 8, 5, 8, 4, 2])