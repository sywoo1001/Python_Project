import plotly
import pandas as pd
from collections import Counter
import plotly.express as px
import re


def add(key):
    f = open('방역.txt', 'r', encoding='utf-8')
    li = f.readlines()

    for l in li:
        if key in l:
            return l.replace(key, '').replace('-','').replace('\t','').replace('종교시설','')


def classify(df):
    for i, s in enumerate(df):
        if "pc방" in s:
            df[i] = "PC방"
        elif "놀이공원" in s:
            df[i] = "놀이공원"
        elif "식당" in s or "음식점" in s:
            df[i] = "음식점"
        elif "카페" in s:
            df[i] = "카페"
        elif "공공기관" in s or '주민센터' in s:
            df[i] = "주민센터"
        elif "병원" in s or "의원" in s or "의료" in s:
            df[i] = "병원"
        elif "무궁화호" in s or "지하철" in s \
                or "KTX" in s or "택시" in s \
                or "버스" in s:
            df[i] = "교통수단"
        elif "미용실" in s or "이발소" in s or "미용" in s or \
                "목욕" in s or "남탕" in s or "여탕" in s or "사우나" in s:
            df[i] = "공중위생업(목욕탕, 미용실 등)"
        elif "유흥업소" in s or "주점" in s or "클럽" in s or '헌팅포자' in s or '콜라텍' in s:
            df[i] = "유흥시설(주점, 콜라텍, 헌팅포차, 클럽 등)"
        elif "헬스장" in s or "체육시설" in s:
            df[i] = "실내체육시설(헬스장, 체육관 등)"
        elif "종교" in s or "교회" in s:
            df[i] = "종교시설"
        elif "동호회" in s or "지인" in s or "모임" in s:
            df[i] = "모임"
        elif "마트" in s or "판매점" in s or "시장" in s or "기계공구" in s or "육가공업" in s or '백화점' in s:
            df[i] = "상점(마트, 가게, 시장, 백화점 등)"
        elif "오락문화" in s or "노래방" in s or "노래연습장" in s:
            df[i] = "오락문화(노래연습장 등)"
        elif "직장" in s or "사무시설" in s or "회사" in s:
            df[i] = "직장"
        elif "학교" in s or "어린이집" in s:
            df[i] = "학교(어린이집, 초·중·고등학교)"
        elif "학원" in s:
            df[i] = "학원"
        else:  # 장소유형 미공개 데이터는 기타로 처리
            df[i] = "기타"

    count = Counter(df)
    del count['기타']

    danger = []
    rule = []
    for k, v in zip(count.keys(), count.values()):
        if v > 50 and v < 100:
            add_str = add(k)
            danger.append('''                    
                    <br>&nbsp;&nbsp;|￣￣￣￣￣￣￣|
                    <br>&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>주의</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
                    <br>&nbsp;&nbsp;|＿＿＿＿＿＿＿| 
                    <br>&nbsp;(＼＿＿／)&nbsp;&nbsp;&nbsp;|| 
                    <br>&nbsp;&nbsp;(  ఠ_ఠ)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|| 
                    <br>&nbsp;&nbsp;&nbsp;/ . . . .づ
                    <br>&nbsp;<b>현황 예의주시 필요</b>
                    <br>=================''' + '<br><현 방역수칙><br>' + add_str)
        elif v >= 100:
            add_str = add(k)
            danger.append('''
                    <br>&nbsp;&nbsp;|￣￣￣￣￣￣￣|
                    <br>&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>위험</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
                    <br>&nbsp;&nbsp;|＿＿＿＿＿＿＿| 
                    <br>&nbsp;(＼＿＿／)&nbsp;&nbsp;&nbsp;|| 
                    <br>&nbsp;&nbsp;(▼ 益 ▼)&nbsp;&nbsp;&nbsp;|| 
                    <br>&nbsp;&nbsp;&nbsp;/ . . . .づ
                    <br>&nbsp;<b>방역강화 필요</b>
                    <br>=================
                    ''' + '<br><현 방역수칙><br>' + add_str)
        else:
            add_str = add(k)
            danger.append('''
                    <br>&nbsp;&nbsp;|￣￣￣￣￣￣￣|
                    <br>&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>유지</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
                    <br>&nbsp;&nbsp;|＿＿＿＿＿＿＿| 
                    <br>&nbsp;(＼＿＿／)&nbsp;&nbsp;&nbsp;|| 
                    <br>&nbsp;&nbsp;(⚆ ͜ʖ ͡⚆)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|| 
                    <br>&nbsp;&nbsp;&nbsp;/ . . . .づ
                    <br>&nbsp;<b>현행유지</b>
                    <br>=================
                    ''' + '<br><현 방역수칙><br>' + add_str)
    ans = pd.DataFrame(count.items(), columns=['업종', '빈도'])
    ans['==============='] = danger
    return ans


if __name__ == "__main__":
    df = pd.read_excel(r'C:\Users\cupid\OneDrive\바탕 화면\새 폴더\Python_Project-naeun\새 폴더\merge_file.xlsx')['장소'].tolist()
    f = classify(df)
    fig = px.pie(f, values='빈도', names='업종', hover_data=['==============='], title='방역 강화 업종 분류')
    fig.show()
    plotly.offline.plot(fig, filename='./result.html')