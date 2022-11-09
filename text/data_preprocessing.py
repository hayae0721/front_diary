from hanspell import spell_checker
from konlpy.tag import Okt  # open korean text (twitter)
import kss  # korean split sentence (한국어 문장 분리기)


# ex1: 쌤이 책읽어주는데 승훈이가 울어서 끗까지 못봐서 승훈이랑 울었다
# result1: 선생님이 책 읽어주는데 승훈이가 울어서 끝까지 못 봐서 승훈이랑 울었다
# ex2: 오늘 내 간식을 앙마같은 내 동생이 다먹었따. 화가난다 난 참지안을것이다
# result2: 오늘 내 간식을 악마 같은 내 동생이 다 먹었다. 화가 난다 난 참지 않을 것이다
def korean_check(text: str):
    result = spell_checker.check(text).as_dict()  # 맞춤범 검사 결과
    dict = {
        0: '문제 없음',
        1: '맞춤법 검사 결과 문제가 없는 단어 또는 구절', 2: '맞춤법에 문제가 있는 단어 또는 구절',
        3: '띄어쓰기에 문제가 있는 단어 또는 구절', 4: '표준어가 의심되는 단어 또는 구절',
        5: '통계적 교정에 따른 단어 또는 구절'
    }
    detail_view = []  # 맞춤범 검사 결과 상세 보기할 시
    morpheme_num = len(result["words"])  # 문장에서의 형태소 개수
    error_num = result["errors"]  # 문장에서 맞춤법 틀린 개수

    for key, value in result['words'].items():
        if value:
            # print(f'문장에 {dict[value]}가 있네요. 옳바르게 고치면 "{key}"으로 해야한답니다.')
            detail_view.append(f'문장에 {dict[value]}가 있네요. 옳바르게 고치면 "{key}"으로 해야한답니다.')

    return result['checked'], detail_view, morpheme_num, error_num


# input: 오늘 내 간식을 악마 같은 내 동생이 다 먹었다. 화가 난다 난 참지 않을 것이다
# output: ['오늘 내 간식을 악마 같은 내 동생이 다 먹었다.', '화가 난다', '난 참지 않을 것이다']
def korean_split_sentence(text: list) -> list:
    return [sentence for sentence in kss.split_sentences(text)]


# 일기 감정 분석을 한 뒤, 부모님(선생님)한테 유저(아이)가 일주일 동안 어떤 단어를 일기에 사용했는지 wordcloud로 보내기 위한 함수
def extract_noun(sentence: list) -> list:
    okt = Okt()  # okt 객체 선언

    return okt.nouns(sentence)


if __name__ == '__main__':
    # 1단계 일기 텍스트 부분 입력받기
    origin_text = str(input())  # 일기 텍스트 맞춤범 검사 원본 받기

    # 2단계 일기 텍스트 부분 맞춤법 검사 후, 옯바르게 수정된 텍스트 가져오기
    # 맞춤법 수정된 문장, 맞춤법 오류 상세 내용, 문장에서의 총 형태소 개수, 맞춤법 틀린 개수
    edit_text, detail_text, morpheme_num, error_num = korean_check(origin_text)

    # 3-1단계 맞춤법 교정된 전체 문장을 소문장별로 분리하기
    sentences = korean_split_sentence(edit_text)

    # 3-2단계 맞춤법 교정된 문장에서 명사만 추출하기
    nouns = extract_noun(edit_text)