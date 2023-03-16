from classify_data import loc
from operator import itemgetter

#2단계 지역 방역수칙
preventionRules = [ "| 음식 섭취 금지(칸막이 내에서 개별 섭취 시 제외)\n| 좌석 한 칸 띄우기(칸막이 있는 경우 제외)\n",
                    "| 포장·배달만 허용\n| 테이블 간 1m 거리두기\n| 좌석/테이블 한 칸 띄우기\n| 테이블 간 칸막이/가림막 설치 중 한 가지 준수(50m² 이상)\n",
                    "| 수용가능인원의 1/3으로 인원 제한\n",
                    "| 마스크 착용 의무화\n| 버스,기차 등 교통수단(차량) 내에서 음식 섭취 금지(국제항공편 제외)\n",
                    "| 21시 이후S로 포장·배달만 허용\n| 테이블 간 1m 거리두기\n| 좌석/테이블 한 칸 띄우기\n| 테이블 간 칸막이/가림막 설치 중 한 가지 준수(50m² 이상)\n",
                    "| 각 부처 및 지자체의 판단에 따라 방역 관리 상황, 시설별 특성 등을 고려하여 일부 탄력적 운영 가능\n",
                    "| 마스크 착용 의무화\n",
                    "| 시설 면적 8㎡당 1명으로 인원 제한 또는 두 칸 띄우기\n| 목욕장업은 음식 섭취 금지\n",
                    "| 집합금지\n",
                    "| 21시 이후 운영 중단\n| 음식 섭취 금지\n| 시설 면적 4㎡당 1명 인원 제한\n",
                    "| 정규예배·미사·법회·시일식 등 좌석 수의 20% 이내 인원 참여\n| 종교활동 주관의 모임·식사는 금지\n",
                    "| 100인 이상의 모임·행사 금지\n",
                    "| 마스크 착용, 환기·소독\n",
                    "| 21시 이후 운영 중단\n| 시설 면적 4㎡당 1명 인원 제한\n| 음식 섭취 금지\n| 이용한 룸은 바로 소독, 30분 후 사용\n",
                    "| 공공기관은 기관별·부서별 적정비율(예: 전 인원의 1/3)재택근무 등 실시\n| 점심시간 시차운영 등 적극 활용(1.5단계 조치와 동일)\n",
                    "| 밀집도 1/3 원칙(고등학교는 2/3)\n| 탄력적 학사 운영 등으로 최대2/3 내에서 운영 가능\n",
                    "| 음식 섭취 금지\n| ①시설 면적 8㎡당 1명으로 인원 제한 또는 두 칸 띄우기 ② 시설 면적 4㎡당 1명으로 인원 제한 또는 한 칸 띄우기 실시하고 21시 이후 운영 중단 중 선택하여 준수\n"
                    ]

for i in range(0, len(loc)):
    loc[i].append(preventionRules[i]) #loc 리스트에 방역수칙 추가([2] 인덱스)


loc.sort(key=itemgetter(1)) # 장소유형 횟수에 따라 오름차순 정렬

frequency = [] #빈도수
labels = [] #장소유형
preventionRulesLabels = [] #방역수칙 공개할 라벨

for i in range(0, len(loc)):
    frequency.append(loc[i][1])
    labels.append(loc[i][0])
    if loc[i][1] > 50:
            preventionRulesLabels.append(loc[i][2]) #방역수칙

            
        

## 데이터 라벨, 빈도수, 색상을 빈도수를 기준으로 정렬해야한다.
labels_frequency = zip(labels,frequency) 
labels_frequency = sorted(labels_frequency,key=lambda x: x[1],reverse=True)
 
labels = [x[0] for x in labels_frequency] ## 정렬된 라벨
frequency = [x[1] for x in labels_frequency] ## 정렬된 빈도수

#matplotlib 패키지 한글 깨짐 처리 시작
import matplotlib.pyplot as plt
import platform
import matplotlib as mpl
if platform.system() == 'Darwin': #맥
        plt.rc('font', family='AppleGothic') 
elif platform.system() == 'Windows': #윈도우
        plt.rc('font', family='Malgun Gothic') 
elif platform.system() == 'Linux': #리눅스 (구글 콜랩)
        #!wget "https://www.wfonts.com/download/data/2016/06/13/malgun-gothic/malgun.ttf"
        #!mv malgun.ttf /usr/share/fonts/truetype/
        #import matplotlib.font_manager as fm 
        #fm._rebuild() 
        plt.rc('font', family='Malgun Gothic') 
plt.rcParams['axes.unicode_minus'] = False #한글 폰트 사용시 마이너스 폰트 깨짐 해결
#matplotlib 패키지 한글 깨짐 처리 끝
mpl.rcParams['font.size'] = 5 #라벨 폰트 사이즈 디폴트값

#파이차트 옵션
import numpy as np
import seaborn as sns

colors = sns.color_palette('hls',len(labels)) ## 라벨의 개수 만큼 색상 리스트 생성 

fig = plt.figure(figsize=(8,10)) ## 캔버스 생성
fig.set_facecolor('white') ## 캔버스 배경색을 하얀색으로 설정
ax = fig.add_subplot() ## 프레임 생성

pie = ax.pie(frequency, ## 파이차트 출력
       startangle=90, ## 시작점을 90도(degree)로 지정
       counterclock=False, ## 시계 방향으로 그린다.
       colors = colors ## 색상 지정
       )

total = np.sum(frequency) ## 빈도수 합
 
threshold = 5 ## 상한선 비율
threshold_none = 2 #표시하지 않을 상한선 비율
sum_pct = 0 ## 퍼센티지
 
bbox_props = dict(boxstyle='square',fc='w',ec='w',alpha=0) ## annotation 박스 스타일
 
## annotation 설정
config = dict(arrowprops=dict(arrowstyle='-'),bbox=bbox_props,va='center')
 
for i,l in enumerate(labels):
    ang1, ang2 = ax.patches[i].theta1, ax.patches[i].theta2 ## 파이의 시작 각도와 끝 각도
    center, r = ax.patches[i].center, ax.patches[i].r ## 원의 중심 좌표와 반지름길이
    
    if i < len(labels) - 1:
        sum_pct += float(f'{frequency[i]/total*100:.2f}')
        text = f'{frequency[i]/total*100:.2f}%'
    else: ## 마지막 파이 조각은 퍼센티지의 합이 100이 되도록 비율을 조절
        text = f'{100-sum_pct:.2f}%'
    
    ## 비율 상한선보다 작은 것들은 Annotation으로 만든다.
    if frequency[i]/total*100 < threshold:
        if frequency[i]/total*100 < threshold_none:
            continue
        ang = (ang1+ang2)/2 ## 중심각
        x = np.cos(np.deg2rad(ang)) ## Annotation의 끝점에 해당하는 x좌표
        y = np.sin(np.deg2rad(ang)) ## Annotation의 끝점에 해당하는 y좌표
        
        ## x좌표가 양수이면 즉 y축을 중심으로 오른쪽에 있으면 왼쪽 정렬
        ## x좌표가 음수이면 즉 y축을 중심으로 왼쪽에 있으면 오른쪽 정렬
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang) ## 시작점과 끝점 연결 스타일
        config["arrowprops"].update({"connectionstyle": connectionstyle}) ## 
        ax.annotate(text, xy=(x, y), xytext=(1.5*x, 1.2*y),
                    horizontalalignment=horizontalalignment, **config)
    else:
        x = (r/2)*np.cos(np.pi/180*((ang1+ang2)/2)) + center[0] ## 텍스트 x좌표
        y = (r/2)*np.sin(np.pi/180*((ang1+ang2)/2)) + center[1] ## 텍스트 y좌표
        ax.text(x,y,text,ha='center',va='center',fontsize=7)

placeTypeLegend = plt.legend(pie[0],labels, bbox_to_anchor=(1,1), loc="upper right", 
                          bbox_transform=plt.gcf().transFigure)
art_lenged_1 = plt.gca().add_artist(placeTypeLegend)
preventionRulesLegend = plt.legend(preventionRulesLabels, bbox_to_anchor=(0.5,0), loc="lower center", bbox_transform=plt.gcf().transFigure)
art_lenged_2 = plt.gca().add_artist(preventionRulesLegend)

plt.show()
