import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

# 추후에  drawing-dirary/text/data-preprocessing.py 에서 명사 List 받아오는걸로 변경
noun_adj_list = ['엄마', '엄마', '엄마', '엄마', '엄마', '엄마', '선생님', '선생님', '꽃', '하늘', '개구리', '공룡', '고래', '아이스크림',
                 '초콜렛', '초콜렛', '초콜렛', '게임', '게임', '아빠', '동생', '고양이', '강아지', '친구', '유튜브']

# 가장 많이 나온 단어부터 40개를 저장한다.
counts = Counter(noun_adj_list)
tags = counts.most_common(40)

# WordCloud를 생성한다.
# 한글을 분석하기위해 font를 한글로 지정해주어야 된다. macOS는 .otf , window는 .ttf 파일의 위치를
# 지정해준다. (ex. '/Font/GodoM.otf')
wc = WordCloud(
    font_path="AppleGothic",
    background_color="white",
    max_font_size=60
)
cloud = wc.generate_from_frequencies(dict(tags))

plt.figure(figsize=(10, 8))
plt.axis('off')
plt.imshow(cloud)

# 화면에 wordcloud 출력
plt.show()

# wordcloud 저장
# cloud.to_file('test.jpg')