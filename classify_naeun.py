import plotly
import pandas as pd
from collections import Counter
import plotly.express as px

def classify(df):
    for i,s in enumerate (df):
        if "pc방" in s:
            df[i]="pc방"
        elif "놀이공원" in s:
            df[i]="놀이공원"
        elif "식당" in s or "음식점" in s or"카페" in s:
            df[i] = "식당/카페"
        elif "공공기관" in s:
            df[i] ="주민센터"
        elif "병원" in s or "의원" in s or "의료" in s:
            df[i] ="병원"
        elif "무궁화호" in s or "지하철" in s \
                or "KTX" in s or "택시" in s \
                or "버스" in s:
            df[i] = "교통수단"
        elif "미용실" in s or "이발소" in s or "미용" in s :
            df[i] = "미용업"
        elif "목욕" in s or "남탕" in s or "여탕" in s or "사우나" in s:
            df[i] = "목욕장업"
        elif "유흥업소" in s or "주점" in s or "클럽" in s:
            df[i] = "유흥시설"
        elif "헬스장" in s or "체육시설" in s:
            df[i] = "실내체육시설"
        elif "종교" in s or "교회" in s:
            df[i] = "종교시설"
        elif "동호회" in s or "지인" in s or "모임" in s:
            df[i] = "모임"
        elif "마트" in s or "판매점" in s or "시장" in s or "기계공구" in s or "육가공업" in s or '백화점' in s:
            df[i] = "상점/마트/백화점"
        elif "오락문화" in s or "노래방" in s or "노래연습장" in s:
            df[i] = "노래연습장"
        elif "직장" in s or "사무시설" in s or "회사" in s:
            df[i] = "직장"
        elif "학교" in s or "어린이집" in s:
            df[i] = "학교"
        elif "학원" in s:
            df[i] = "학원"
        else:  # 장소유형 미공개 데이터는 기타로 처리
            df[i] = "기타"


    count=Counter(df)
    del count['기타']

    danger=[]
    for v in count.values():
        if v>50 and v<100:
            danger.append('주의<br>======<br>현황 예의주시 필요<br>======<br>'
                      '<방역 수칙><br>'
                      '마스크 착용 의무화<br>'
                      '21시 이후 운영 중단<br>'
                      '좌석 한 칸 띄우기<br>'
                      '시설 면적 4m^2 혹은 8m^2 당 한명으로 인원 제한<br>'
                      '기타 등등<br>'
                      '출처:보건복지부')
        elif v>=100:
            danger.append('위험<br>======<br>방역강화 필요<br>ex)운영제한 및 집합금지<br>======<br>'
                      '<방역 수칙><br>'
                      '마스크 착용 의무화<br>'
                      '21시 이후 운영 중단<br>'
                      '좌석 한 칸 띄우기<br>'
                      '시설 면적 4m^2 혹은 8m^2 당 한명으로 인원 제한<br>'
                      '기타 등등<br>'
                      '출처:보건복지부')
        else:
            danger.append('안전<br>======<br>현행유지<br>======<br>'
                          '<방역 수칙><br>'
                          '마스크 착용 의무화<br>'
                          '21시 이후 운영 중단<br>'
                          '좌석 한 칸 띄우기<br>'
                          '기타 등등<br>'
                          '출처:보건복지부')
    ans=pd.DataFrame(count.items(), columns=['업종', '빈도'])
    ans['위험도'] =danger
    return ans

if __name__ == "__main__":
    df=pd.read_excel(r'C:\Users\cupid\OneDrive\바탕 화면\Python_Project-naeun\새 폴더\merge_file.xlsx')['장소'].tolist()
    f=classify(df)
    fig = px.pie(f, values='빈도', names='업종', hover_data=['위험도'], title='방역 강화 업종 분류')
    fig.show()
    plotly.offline.plot(fig, filename='./result.html')
